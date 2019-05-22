"""
Django settings for orchy_project project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j%5fm=ryk!m*_ad=^yy%m(^@8_-!rx))&hm$t29f%e$1!x-hkh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'api.User'

DEFAULT_USER_EMAIL = 'admin@gmail.org'

OWASP_TYPES = [
    'Injection',
    'Broken Authentication and Session Management',
    'Cross-Site Scripting',
    'Insecure Direct Object References',
    'Security Misconfiguration',
    'Sensitive Data Exposure',
    'Missing Function Level Access Control',
    'Cross-Site Request Forgery',
    'Using Components with Known Vulnerabilities',
    'Unvalidated Redirects and Forwards',
    'Uncategorized'
]

VULNERABILITY_TYPES = ['Coding','Design','Configuration']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'background_task',
    'api',
    'corsheaders',
    # 'rest_framework_filters',
    # 'django_extensions'
]

SITE_ID = 1

CORS_ORIGIN_ALLOW_ALL = DEBUG

CORS_ORIGIN_WHITELIST = (
    # 'localhost:8000',
    'localhost:8080',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

JANATHA_CLASS = [16,200,295]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'orchy_project.middleware.ExceptionMiddleware',
]

ROOT_URLCONF = 'orchy_project.urls'
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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
WSGI_APPLICATION = 'orchy_project.wsgi.application'
DB_IP = os.environ.get('DB_IP', '127.0.0.1')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
FROM_EMAIL = os.environ.get('FROM_EMAIL')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'orchy_community',# Or path to database file if using sqlite3.
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'hegemony86'),
        'HOST': DB_IP,# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('DB_PORT', 3306), # Set to empty string for default 3306.
    },
    "OPTIONS": {
        "init_command": "SET SESSION group_concat_max_len = 1000000;"
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

# from api.password_validators import PasswordValidator

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'api.password_validators.PasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FILE_SIZE_LIMIT = 20

FILE_UPLOAD_MAX_MEMORY_SIZE = FILE_SIZE_LIMIT * 1024 * 1024


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
   'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
   ),
   'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
   'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
    # 'EXCEPTION_HANDLER': 'orchy_project.exception_handler.custom_exception_handler'
}


minio_url = os.environ.get('MINIO_URL')
minio_port = os.environ.get('MINIO_PORT')

MINIO = {
    'bucket_name':os.environ.get('MINIO_BUCKET_NAME'),
    'access_key':os.environ.get('MINIO_ACCESS_KEY'),
    'secret_key':os.environ.get('MINIO_SECRET_KEY'),
    'url': '{0}:{1}'.format(minio_url, minio_port)
}


WEBHOOK_TOOLS = {
    'Orchestron JSON':'json',
    'ZAP':'json,xml',
    'Burp':'json,xml',    
    'OWASP Dependency Checker':'xml',    
    'FindSecBugs':'xml'    
}


HEADER_MAP = {
    'issues':'Burp',
    'OWASPZAPReport':'ZAP',    
    'analysis':'OWASP Dependency Checker',    
    'BugCollection':'FindSecBugs'
}


PLATFORMS = ['ASP.NET','JAVA','Python','Ruby','Node/JavaScript','PHP']


HOST_TYPES = ['Web Application','Web Services','Mobile Application','IoT Application']


SCAN_STATUS = ['Uploaded','In Progress','Completed','Stopped','Initiated','Failed','Killed']


JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'api.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': os.environ.get('JWT_SECRET_KEY'),
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}






LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'debug_log':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
        'critical_log':{
            'level': 'CRITICAL',
            'class': 'logging.StreamHandler'
        },
        'warning_log':{
            'level': 'WARNING',
            'class': 'logging.StreamHandler'
        },
        'error_log':{
            'level': 'ERROR',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'background_task.tasks': {
            'handlers': ['debug_log','error_log','warning_log','critical_log'],
            'level': 'INFO'
        },
    }
}


# BACKGROUND_TASK_RUN_ASYNC = True

# BACKGROUND_TASK_ASYNC_THREADS = 10


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'api/media/')
PARSERS_ROOT = os.path.join(BASE_DIR, 'parsers/')
FONT_ROOT = os.path.join(BASE_DIR, 'api/fonts/')
EMAIL_TEMPLATE = os.path.join(BASE_DIR, 'api/template/')
MEDIA_URL = '/media/'
PROJECT_MEDIA_URL = 'project_logo/'
APPLICATION_MEDIA_URL = 'app_logo/'
ORGANIZATION_MEDIA_URL = 'logo/'
USER_MEDIA_URL = 'img/'

TEST_DATA_ROOT = os.path.join(MEDIA_ROOT,'testdata')

XML_ROOT = os.path.join(MEDIA_ROOT,'xml_files')

ML_FILE_ROOT = os.path.join(MEDIA_ROOT,'ml_files')

EVIDENCE_ROOT = os.path.join(MEDIA_ROOT,'Evidence')
EVIDENCE_MEDIA_URL = 'Evidence/'

REMEDIATION_ROOT = os.path.join(MEDIA_ROOT,'remedy_files')
REMEDY_MEDIA_URL = 'remedy_files/'

EVIDENCE_REMEDIATION_ROOT = os.path.join(MEDIA_ROOT,'evid_remedy_files')
EVIDENCE_REMEDY_MEDIA_URL = 'evid_remedy_files/'
