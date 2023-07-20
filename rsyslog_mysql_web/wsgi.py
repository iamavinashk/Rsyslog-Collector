
import os
import sys

path = '/opt/python'
if path not in sys.path:
    sys.path.append(path)
    
path = '/opt/python/rsyslog_mysql_web'
if path not in sys.path:
    sys.path.append(path)
    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rsyslog_mysql_web.settings")


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
