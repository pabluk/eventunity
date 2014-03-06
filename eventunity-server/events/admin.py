from django.contrib.gis import admin
from events.models import Community, Event


class EventAdmin(admin.GeoModelAdmin):
    list_display = ('community', 'name', 'location', 'date')
    list_display_links = ('name',)
    list_filter = ('community__name',)

admin.site.register(Community)
admin.site.register(Event, EventAdmin)
