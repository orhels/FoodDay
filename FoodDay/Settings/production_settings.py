# coding=UTF-8
from base_settings import *

I_AM_ONLY_DOING_THIS_TO_TRICK_PYCHARMS


import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

