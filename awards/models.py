from django.utils import timezone
from django.db import models
from django.urls import reverse
from account.models import Account


class Award(models.Model):
    EMPLOYEE_OF_THE_YEAR = 'Employee of the Year'
    EMPLOYEE_OF_THE_MONTH = 'Employee of the Month'
    EMPLOYEE_OF_THE_WEEK = 'Employee of the Week'
    AWARD_CATEGORY_TYPES = [
        (EMPLOYEE_OF_THE_YEAR, 'Employee of the Year'),
        (EMPLOYEE_OF_THE_MONTH, 'Employee of the Month'),
        (EMPLOYEE_OF_THE_WEEK, 'Employee of the Week'),
    ]
    category = models.CharField('category', max_length=120, blank=False, choices=AWARD_CATEGORY_TYPES,
                                default=EMPLOYEE_OF_THE_YEAR)
    region = models.CharField('region', max_length=120, blank=False)
    date_created = models.DateTimeField('created', default=timezone.now, null=True)
    date_granted = models.DateTimeField('date granted', blank=True)
    submitter = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    recipient_fname = models.CharField('recipient first name', max_length=120, blank=False)
    recipient_lname = models.CharField('recipient last name', max_length=120, default=None)
    recipient_email = models.EmailField('recipient email', max_length=120, blank=False)
    certificate_image = models.CharField(max_length=120, default=None, null=True)

    # this dunder method forces objects in the database to
    # print as a category instead of <QuerySet [<Award:Award object (1)>]
    # when running the Award.objects.all() command in the python shell
    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('award-detail', kwargs={'pk': self.pk})