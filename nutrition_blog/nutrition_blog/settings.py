from pathlib import Path

from .secret_info import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = secret_info.get('SECRET_KEY')

DEBUG = secret_info.get('DEBUG', False)

ALLOWED_HOSTS = (
        '127.0.0.1',
        'localhost',
        'python-web-framework-nutrition.herokuapp.com',
)

# Application definition

DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

)

WEB_APP = (
        'nutrition_blog.web',
        'nutrition_blog.accounts',
        'nutrition_blog.email_client',
)

THIRD_PARTY_APP = (

        'django_celery_results',

)

INSTALLED_APPS = WEB_APP + DJANGO_APPS + THIRD_PARTY_APP

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nutrition_blog.urls'

TEMPLATES = [
        {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'nutrition_blog.wsgi.application'

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
        }
}

# DATABASES = {
#         'default': {
#                 'ENGINE': 'django.db.backends.postgresql',
#                 'NAME': secret_info.postgres_info['database'],
#                 'USER': secret_info.postgres_info['user'],
#                 'PASSWORD': secret_info.postgres_info['password'],
#                 'HOST': secret_info.postgres_info['host'],
#                 'PORT': secret_info.postgres_info['port'],
#         }
# }

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = (
        BASE_DIR / 'static',
)
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# what is the user model app in use
AUTH_USER_MODEL = 'accounts.AppUser'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = secret_info.get('EMAIL_HOST')
EMAIL_PORT = secret_info.get('EMAIL_port')
EMAIL_USE_TLS = secret_info.get('EMAIL_USE_TLS')
EMAIL_HOST_USER = secret_info.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = secret_info.get('EMAIL_HOST_PASSWORD')

# redis configuration
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# django-celery-result configuration

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

# reCaptcha

RECAPTCHA_PUBLIC_KEY = RECAPTCHA_PUBLIC_KEY_RECAPTCHA
RECAPTCHA_PRIVATE_KEY = RECAPTCHA_PRIVATE_KEY_RECAPTCHA
