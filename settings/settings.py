import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^mv8y^rz8$uhqdbx^*^ol&kl_a%7egev_oyp+g-3q5ax--qmb@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# When DEBUG = False put Domains here like: www.example.com and example.com
ALLOWED_HOSTS = ['http://www.localhost:8000/']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'apps.administrator.main',
    'apps.administrator.exams',
    'apps.api'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'settings.middlewares.StripWhitespaceMiddleware',
)

ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'
# Custom 403 for CSRF failure whe in Production
CSRF_FAILURE_VIEW = 'settings.error_views.csrf_failure'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.context_processors.site_name',
            ],
        },
    },
]

# Defaul configs for Administrator to work
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
PASSWORD_RESET_TIMEOUT_DAYS = 1

# Production Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NAMEDB',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True

# Time zone false enables the use of datetime for easier calculations
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# In production UNCOMMENT THIS
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = ()

# Media Server Config
# Only for UPLOADED files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Email Server
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'layerdd@gmail.com'
EMAIL_HOST_PASSWORD = 'layerddlayer'
TO = "contact@client.com.br"
SENDER_HEADER = "Client <"+EMAIL_HOST_USER+">"

# Set the SITE_NAME, by default included in all templates and website_base.html on the title
SITE_NAME = "YOUR WEBSITE NAME"
# Set Site id of SitesFramework
SITE_ID = 2

# API settings
API_ON = True

# Logging configs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
