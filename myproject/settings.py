"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import datetime
import dj_database_url
import cloudinary
import cloudinary_storage



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xrf5i(gv3ttr9fqyj924gro#q0-nrykwxs+*21753^%qoj*+3e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

if DJANGO_ENV == 'production':
    ALLOWED_HOSTS = ['food-exchange-86c863cfe30c.herokuapp.com']
else:
    ALLOWED_HOSTS = ['*']

if DJANGO_ENV == 'production':
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'CLOUDINARY_CLOUD_NAME',
        'API_KEY': 'CLOUDINARY_API_KEY',
        'API_SECRET': 'CLOUDINARY_API_SECRET',
    }

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# Application definition
#'app.apps.AppConfig',

INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

ASGI_APPLICATION = 'myproject.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.environ.get('USE_HEROKU_DB') == 'true':
    db_config = dj_database_url.config(default=os.environ.get('JAWSDB_URL'))
    DATABASES = {
        'default': db_config
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_db',
            'USER': 'django',
            'PASSWORD': 'password',
            'HOST': 'db',
        }
    }

AUTH_USER_MODEL = 'app.CustomUser'





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)/doc
# https:/s.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

if DJANGO_ENV == 'production':
    MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHNTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

SWESSION_COOKIE_SECURE = False

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

DATE_FORMAT = 'Y-m-d'