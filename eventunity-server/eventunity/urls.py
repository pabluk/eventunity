from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventunity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'events.views.index', name='index'),

    url(r'^api/home/$', 'events.views.home', {'coordinates': None, 'distance': 0}),
    url(r'^api/home/(?P<coordinates>[\d\-\.,]+)/$', 'events.views.home', {'distance': 500}),
    url(r'^api/home/(?P<coordinates>[\d\-\.,]+)/(?P<distance>\d+)/$', 'events.views.home'),
    url(r'^api/communities/$', 'events.views.communities', name='communities'),
    url(r'^api/events/$', 'events.views.events', name='events'),
    url(r'^api/events/(?P<event_id>\d+)/$', 'events.views.event_detail', name='event_detail'),
    url(r'^api/events/location/(?P<coordinates>[\d\-\.,]+)/$', 'events.views.events_by_location', {'distance': 500}),
    url(r'^api/events/location/(?P<coordinates>[\d\-\.,]+)/(?P<distance>\d+)/$', 'events.views.events_by_location'),
    url(r'^api/events/community/(?P<community_id>\d+)/$', 'events.views.events_by_community', name='events_by_community'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
