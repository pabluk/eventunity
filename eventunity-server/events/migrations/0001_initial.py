# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Community'
        db.create_table(u'events_community', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'events', ['Community'])

        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('community', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Community'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'events', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Community'
        db.delete_table(u'events_community')

        # Deleting model 'Event'
        db.delete_table(u'events_event')


    models = {
        u'events.community': {
            'Meta': {'object_name': 'Community'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Community']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['events']