"""
WSGI config for crispr_porject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VSR.settings")

application = get_wsgi_application()
# import os
# import sys
# sys.path.append('/home/qiusuo/miniconda3/lib/python3.6/site-packages')
# path = '/var/www/html/VSR'
# if path not in sys.path:
#     sys.path.append('/var/www/html/VSR')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VSR.settings")
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
