"""
WSGI config for ten_give project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application


#sys.path.append('/usr/local/lib/python3.9/dist-packages')
sys.path.append('/var/www/ten_give')
sys.path.append('/var/www/ten_give/ten_give')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ten_give.settings')

application = get_wsgi_application()
