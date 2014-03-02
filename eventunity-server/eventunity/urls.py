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

    url(r'^api/communities/$', 'events.views.communities', name='communities'),
    url(r'^api/communities/(?P<community_id>\d+)/events/$', 'events.views.events_by_community', name='events_by_community'),
    url(r'^api/events/$', 'events.views.events', name='events'),
    url(r'^api/events/(?P<event_id>\d+)/detail/$', 'events.views.event_detail', name='event_detail'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
