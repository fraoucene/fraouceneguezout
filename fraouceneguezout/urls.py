from django.conf.urls import patterns, include, url
from django.contrib import admin

from .settings import INSTALLED_APPS, PARTIAL_DIR


# Django URLs
urlpatterns = patterns('',
    url(r'^$', 'fraouceneguezout.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/resume/', include('resume.urls')),
    url(r'^partials/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PARTIAL_DIR}),
)

# Grappelli URLs
if 'grappelli' in INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^grappelli/', include('grappelli.urls')),)
