import json

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from events.models import Community, Event


class Command(BaseCommand):
    args = 'community_id file.json'
    help = 'Import a json file with events'

    def handle(self, *args, **options):
        community_id = args[0]
        filename = args[1]

        with open(filename) as f:
            events = json.load(f)

        community = Community.objects.get(pk=community_id)
        count = 0
        for data in events:
            try:
                Event.objects.get(community=community, url=data['url'])
            except Event.DoesNotExist:
                data['community'] = community
                if data['coordinates']:
                    lng = data['coordinates']['lng']
                    lat = data['coordinates']['lat']
                    data['coordinates'] = Point(lng, lat)
                event = Event(**data)
                event.save()
                count += 1
        print "%d events added." % count
