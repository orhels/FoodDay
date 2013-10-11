# coding=UTF-8
from base_settings import *

I_AM_ONLY_DOING_THIS_TO_TRICK_PYCHARMS

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'foodaytest',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'foodaytest',
        'PASSWORD': 'c*rw1ÞY8w$HÞæwÝ',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}