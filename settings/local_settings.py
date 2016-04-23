import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
TO = 'vinibiso@gmail.com'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #mysql
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #name DB
    }
}
