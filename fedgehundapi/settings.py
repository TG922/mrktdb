"""
Django settings for fedgehundapi project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

env = environ.Env()

# reading .env file
environ.Env.read_env()

DJANGO_ENV = env("ENV", default="development")

# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_ENV == "production":
    DEBUG = True  # Change this to false when deploying final app
else:
    DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DJANGO_ENV == "production":
    # Use hosted remote DB in production
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': env("PRODUCTION_DB_NAME"),
            'CLIENT': {
                'host': env("HOST_IP"),
                'port': int(env("HOST_PORT")),
                'username': env("PRODUCTION_DB_USERNAME"),
                'password': env("PRODUCTION_DB_PASSWORD"),
                'authSource': env("PRODUCTION_DB_NAME"),
            },
        }
    }
else:
    #Use local DB in development
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': env('LOCAL_DB_NAME', default=''),
        }
    }

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'SECRET_KEY', default='f9y!yh1nb6lm5(o*)^(8+-dueu9_p=p$c$d-u8f(p=w+mtd%rx')

ALLOWED_HOSTS = ['mrktdbapi-prod.eba-tw27jjhn.us-west-2.elasticbeanstalk.com','127.0.0.1']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'fedgehund_auth',
    'fedgehund_profile.apps.FedgehundProfileConfig',
    'edgar.apps.EdgarConfig',
    'filer.apps.FilerConfig',
    'testapp',
    'fedgehundui',
    'django_cron',
]

SITE_ID=1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
#The username field is optional and we will hide it in the registration page
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fedgehundapi.urls'

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

WSGI_APPLICATION = 'fedgehundapi.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

CRON_CLASSES = [
    "edgar.cikCusipCronJob.CikCusipCronJob",
    "edgar.securityLinkCompanyCronJob.SecurityLinkCompanyCronJob",
]
