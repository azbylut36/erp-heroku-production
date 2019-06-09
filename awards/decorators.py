from django.core.exceptions import PermissionDenied


def not_admin(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_staff == 'true':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
