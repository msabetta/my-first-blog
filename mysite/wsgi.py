"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

select = 0

if select is not 0:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings.production'


application = get_wsgi_application()
