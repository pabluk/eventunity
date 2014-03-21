from django.core.management.base import BaseCommand

from events.models import Community


class Command(BaseCommand):
    help = 'List registered communities'

    def handle(self, *args, **options):
        communities = Community.objects.order_by('id')
        for c in communities:
            print("Id:%s Name:%s" % (c.id, c.name))
        print("Done.")
