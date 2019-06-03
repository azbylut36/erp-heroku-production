"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# import module for django heroku
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'n3#53bd8gu4o=w$iz$csgq$n!!%ano6pl=g1m+k_2=e3f^t^s='
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DEBUG_VALUE')

ALLOWED_HOSTS = ['theerponeteam.herokuapp.com', 'theerponeteamproduction.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'corsheaders',
    'rest_framework',

    # our ERP models
    'account.apps.AccountConfig',
    'awards.apps.AwardsConfig',

    # 3rd party
    'crispy_forms',
    'django_tex',
    'django_tables2',
    'report_builder'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'backend.urls'

# for testing our backend api only
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'account/templates'),
            os.path.join(BASE_DIR, 'awards/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'NAME': 'tex',
        'BACKEND': 'django_tex.engine.TeXEngine',
        'DIRS': [
            os.path.join(BASE_DIR, 'awards/templates/awards/award_cert'),
        ],
        'APP_DIRS': True,
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    # I removed these because it was annoying in dev. Not sure if we care about these in our prod
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Cors whitelist to prevent cors security. Currently just allowing all
# CORS_ORIGIN_WHITELIST = (
#      'localhost:3000/'
# )
CORS_ORIGIN_ALLOW_ALL = True


# this makes it so that all django pre-built stuff interact and use our Account instead of User as basis of security
AUTH_USER_MODEL = 'account.Account'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'login_success'
LOGIN_URL = 'login'

# NOTE: using os.path.join makes sure that the full path is created correctly
# Base dir tells os where to store media files, in this case sig pics

# Using gmail smtp to send out our emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#EMAIL_HOST_USER = 'erp1.spring2019'
#EMAIL_HOST_PASSWORD = 'erp1@cs467'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# this prevents users from overwriting existing files in the 
# storage bucket with the same name
AWS_S3_FILE_OVERWRITE = False

# requirement from django-storages documentation
AWS_DEFAULT_ACL = None

# from django-storages documentation, which sets S3 as place to store files
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # from the article

# keys to AWS S3 storage bucket which are stored in environment variables, so
# make sure the variables are defined in macOS .bash_profile with actual values
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# This will make sure that the file URL does not have unnecessary parameters like your access key
# from the article
# AWS_QUERYSTRING_AUTH = False

#AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'  # from the article

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
#STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/' # from the article
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/' # Our pics will go in this directory 
#MEDIA_URL = STATIC_URL + 'media/'  # from the article
#STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), ) #new
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_ROOT = 'staticfiles'. #from the article
#ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/' #new

# new 
#STATICFILES_FINDERS = (
#'django.contrib.staticfiles.finders.FileSystemFinder',
#'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#)

# will automatically set some configurations for heroku use
django_heroku.settings(locals())

# latex interpreter
LATEX_INTERPRETER = 'pdflatex'

# settings for django-report-builder
REPORT_BUILDER_INCLUDE = [
    'account.account',
    'awards.award',
    'users_to_awards.accounttoaward'
]
