import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "info.settings")
from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0,PROJECT_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
