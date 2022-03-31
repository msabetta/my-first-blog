from .default import *

ALLOWED_HOSTS = ['msabetta.pythonanyware.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR_TEST = os.path.dirname(os.path.abspath("__file__")) + "/mysite/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR_TEST, 'db_test.sqlite3'),
    }
}


