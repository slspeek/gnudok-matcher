# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WorkLoad.start_time'
        db.add_column(u'main_workload', 'start_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(8, 45)),
                      keep_default=False)

        # Adding field 'WorkLoad.stop_time'
        db.add_column(u'main_workload', 'stop_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(17, 15)),
                      keep_default=False)

        # Adding field 'WorkLoad.user_comment'
        db.add_column(u'main_workload', 'user_comment',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WorkLoad.start_time'
        db.delete_column(u'main_workload', 'start_time')

        # Deleting field 'WorkLoad.stop_time'
        db.delete_column(u'main_workload', 'stop_time')

        # Deleting field 'WorkLoad.user_comment'
        db.delete_column(u'main_workload', 'user_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.capability': {
            'Meta': {'object_name': 'Capability'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.employee': {
            'Meta': {'object_name': 'Employee'},
            'capabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Capability']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'main.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.shift': {
            'Meta': {'object_name': 'Shift'},
            'day_of_week': ('django.db.models.fields.IntegerField', [], {}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(8, 45)'}),
            'stop_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(17, 15)'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Task']"})
        },
        u'main.task': {
            'Meta': {'object_name': 'Task'},
            'capability': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Capability']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.workload': {
            'Meta': {'object_name': 'WorkLoad'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shift': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Shift']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(8, 45)'}),
            'stop_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(17, 15)'}),
            'user_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['main']