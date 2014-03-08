import datetime

from django.contrib.gis.db import models
from django.template.defaultfilters import linebreaksbr


class Community(models.Model):
    name = models.CharField(max_length=200)
    logo = models.FileField(upload_to='logos')

    class Meta:
        verbose_name_plural = 'communities'

    def __unicode__(self):
        return self.name

    def to_json_dict(self):
        today = datetime.date.today()
        json_dict = {
            'id': self.id,
            'name': self.name,
            'logo': self.logo.url,
            'events_count': self.event_set.filter(date__gte=today).count()
        }
        return json_dict


class Event(models.Model):
    name = models.CharField(max_length=200)
    community = models.ForeignKey('Community')
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    url = models.URLField(max_length=1024)
    description = models.TextField()
    coordinates = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    def to_json_dict(self):
        json_dict = {
            'id': self.id,
            'name': self.name,
            'community': self.community.to_json_dict(),
            'date': self.date.strftime("%A, %B %d, %Y"),
            'location': self.location,
            'url': self.url,
            'description': linebreaksbr(self.description)
        }
        return json_dict

    def to_json_dict_reduced(self):
        json_dict = {
            'id': self.id,
            'name': self.name,
            'date': self.date.strftime("%A, %B %d, %Y"),
            'location': self.location,
            'url': self.url
        }
        return json_dict
