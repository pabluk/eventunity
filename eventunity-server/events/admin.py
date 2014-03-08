import datetime

from django.contrib.admin import SimpleListFilter
from django.contrib.gis import admin

from events.models import Community, Event


class EventDateFilter(SimpleListFilter):
    title = 'date'
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        return (
            ('upcoming', 'Upcoming'),
            ('expired', 'Expired'),
        )

    def queryset(self, request, queryset):
        today = datetime.date.today()
        if self.value() == 'upcoming':
            return queryset.filter(date__gte=today)
        if self.value() == 'expired':
            return queryset.filter(date__lt=today)

class EventAdmin(admin.OSMGeoAdmin):
    list_display = ('community', 'name', 'date', 'location', 'coordinates')
    list_display_links = ('name',)
    list_filter = ('community__name', EventDateFilter)

admin.site.register(Community)
admin.site.register(Event, EventAdmin)
