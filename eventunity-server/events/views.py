import datetime

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.shortcuts import render_to_response, get_object_or_404

from events.models import Community, Event
from events.utils import json_response
from events.nominatim import Geocoder


def index(request):
    return render_to_response('index.html')


@json_response
def home(request, coordinates, distance):
    today = datetime.date.today()

    local_events = {'events': [], 'events_total': 0}
    if coordinates:
        lat, lng = coordinates.split(',')
        location = Point([float(lng), float(lat)])
        events_qs = Event.objects.filter(coordinates__distance_lte=(location, D(km=distance)), date__gte=today).order_by('date')
        local_events['events'] = [e.to_json_dict_reduced() for e in events_qs[:5]]
        local_events['events_total'] = events_qs.count()

    communities = [c.to_json_dict() for c in Community.objects.all()]

    data = {
        'local_events': local_events,
        'communities': communities,
    }
    return data


@json_response
def communities(request):
    communities = Community.objects.all()
    return [c.to_json_dict() for c in communities]


@json_response
def events(request):
    today = datetime.date.today()
    events = Event.objects.filter(date__gte=today).order_by('date')
    return [e.to_json_dict() for e in events]


@json_response
def events_by_community(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    today = datetime.date.today()
    events = Event.objects.filter(community=community, date__gte=today).order_by('date')
    return [e.to_json_dict_reduced() for e in events]


@json_response
def events_by_location(request, coordinates, distance):
    lat, lng = coordinates.split(',')
    location = Point([float(lng), float(lat)])
    today = datetime.date.today()
    events = Event.objects.filter(coordinates__distance_lte=(location, D(km=distance)), date__gte=today).order_by('date')
    return [e.to_json_dict_reduced() for e in events]


@json_response
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return event.to_json_dict()


@json_response
def locations(request, name):
    """Search locations by name using the Geocoder API."""
    g = Geocoder()
    location = g.search(name)
    return location
