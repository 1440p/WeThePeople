"""
WSGI config for WeThePeople project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

# Web Server Gateway Interface
# Used as a calling Convention to Forward Server requests
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WeThePeople.settings")

application = get_wsgi_application()
