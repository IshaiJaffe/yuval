from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sites/(?P<pageCMS_id>\d+)/$', 'sites.views.detail'),
    url(r'^sites/add/$', 'sites.views.add'),

    url(r'^contacts/$', 'contacts.views.index'),
    url(r'^contacts/(?P<Contact_id>\d+)/$', 'contacts.views.detail'),
    url(r'^contacts/add/$', 'contacts.views.add'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^me$', 'sites.views.me'),
    url(r'^page/(?P<page_name>\w+)$', 'sites.views.page'),
    url(r'', 'sites.views.index'),
)
