"""
WSGI config for demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

application = get_wsgi_application()

#add the project path in to the sys path
sys.path.append('/var/www/html/project/demo/')

#add the venv site-packages to the sys.path
sys.path.append('var/www/html/project/django/lib/python3.6/site-packages')
