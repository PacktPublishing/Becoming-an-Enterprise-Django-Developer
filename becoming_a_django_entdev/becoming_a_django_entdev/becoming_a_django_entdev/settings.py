"""
Django settings for becoming_a_django_entdev project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath
import django_heroku
import dj_database_url
import dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e8a4a113-8637-41f4-be33-5c707fc9b3fc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'mikedinder.com',
    'www.mikedinder.com',
    'dev.mikedinder.com',
    'staging.mikedinder.com',
    'becoming-an-entdev.herokuapp.com',
    'mighty-sea-09431.herokuapp.com',
    'pure-atoll-19670.herokuapp.com',
]

# Application References
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
DJANGO_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'address',
    'djmoney',
    'phone_field',
]

LOCAL_APPS = [
    'becoming_a_django_entdev.chapter_1',
    'becoming_a_django_entdev.chapter_2',
    'becoming_a_django_entdev.chapter_3',
]

#### MERGE ALL APPS ####
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'becoming_a_django_entdev.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'becoming_a_django_entdev.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Django 3.2 Default Auto ID (Primary Key Setting)
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'chapter_3.Seller'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Django-Money Field Package
CURRENCIES = ('USD', 'EUR')
CURRENCY_CHOICES = [
    ('USD', 'USD $'),
    ('EUR', 'EUR €'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

django_heroku.settings(locals())

options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)

try:
    from .local_settings import *
except ImportError:
    pass
