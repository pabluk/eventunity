from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos')

    class Meta:
        verbose_name_plural = 'communities'

    def __unicode__(self):
        return self.name

    def to_json_dict(self):
        json_dict = {
            'id': self.id,
            'name': self.name,
            'logo': self.logo.url
        }
        return {'id': self.id, 'name': self.name, 'logo': self.logo.url}


class Event(models.Model):
    name = models.CharField(max_length=200)
    community = models.ForeignKey('Community')
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    url = models.URLField(max_length=1024)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    def to_json_dict(self):
        json_dict = {
            'name': self.name,
            'community': self.community.to_json_dict(),
            'date': self.date.strftime("%A, %B %d, %Y"),
            'location': self.location,
            'url': self.url,
            'description': self.description
        }
        return json_dict

    def to_json_dict_reduced(self):
        json_dict = {
            'name': self.name,
            'date': self.date.strftime("%A, %B %d, %Y"),
            'location': self.location,
        }
        return json_dict
