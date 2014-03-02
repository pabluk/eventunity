import datetime

from django.shortcuts import render_to_response, get_object_or_404

from events.models import Community, Event
from events.utils import json_response


def index(request):
    return render_to_response('index.html')


@json_response
def communities(request):
    communities = Community.objects.all()
    return [c.to_json_dict() for c in communities]


@json_response
def events_by_community(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    today = datetime.date.today()
    events = Event.objects.filter(community=community, date__gte=today).order_by('date')
    return [e.to_json_dict_reduced() for e in events]


@json_response
def events(request):
    today = datetime.date.today()
    events = Event.objects.filter(date__gte=today).order_by('date')
    return [e.to_json_dict() for e in events]


@json_response
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return event.to_json_dict()
