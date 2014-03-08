# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Community.logo'
        db.alter_column(u'events_community', 'logo', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Community.logo'
        db.alter_column(u'events_community', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'events.community': {
            'Meta': {'object_name': 'Community'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Community']"}),
            'coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['events']