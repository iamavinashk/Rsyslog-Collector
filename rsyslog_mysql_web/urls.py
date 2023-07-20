

from django.urls import include, path
from django.conf import settings
from django.views.static import serve
from logviewer.views import index,flexigridajax
import os


urlpatterns = [
    path('', index, name='rsyslog'),
    path('ajax', flexigridajax, name='flexigridajax'),
    
]

# static files in debug mode (e.g., CSS)
if settings.DEBUG:
    urlpatterns += [
        path('site_media/<path:path>', serve, {'document_root': os.path.join(os.path.dirname(__file__), 'site_media').replace('\\', '/')}),
    ]
