"""
Django settings for django_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2zt$lngj&u78-$4mxjsbq__eu32(h^#lx9&#wc0b#)le^%38i9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []
#template url

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)



TEMPLATE_DIRS = (
    #os.path.join(PROJECT_DIRECTORY,'templates/'),
    #os.path.join(PROJECT_DIRECTORY,'articles/templates/'),
    '/home/pawan/Desktop/django_test/templates',
    '/home/pawan/Desktop/django_test/article/templates',
    '/home/pawan/Desktop/django_test/edu_articles/templates',
    '/home/pawan/Desktop/django_test/poli_article/templates',
    '/home/pawan/Desktop/django_test/E_article/templates',
    '/home/pawan/Desktop/django_test/sci_article/templates',
    '/home/pawan/Desktop/django_test/userprofile/templates',
     #os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)




# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    'userprofile',
    'article',
    'poli_articles',
    'edu_articles',
    'E_articles',
    'sci_articles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_test.urls'

WSGI_APPLICATION = 'django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'thinks.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Greenwich'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/home/rahul/django-mike/django_test/static/'

