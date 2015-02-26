from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^cached-asset/(?P<asset>.*)$', 'appmedia.views.serve_cached_asset', name="cached_asset"),
    (r'^(?P<app>[^/]*)/(?P<path>.*)$', 'appmedia.views.serve'),
)
