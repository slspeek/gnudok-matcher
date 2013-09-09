# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Capability'
        db.create_table(u'main_capability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['Capability'])

        # Adding model 'Employee'
        db.create_table(u'main_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'main', ['Employee'])

        # Adding M2M table for field capabilities on 'Employee'
        db.create_table(u'main_employee_capabilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employee', models.ForeignKey(orm[u'main.employee'], null=False)),
            ('capability', models.ForeignKey(orm[u'main.capability'], null=False))
        ))
        db.create_unique(u'main_employee_capabilities', ['employee_id', 'capability_id'])


    def backwards(self, orm):
        # Deleting model 'Capability'
        db.delete_table(u'main_capability')

        # Deleting model 'Employee'
        db.delete_table(u'main_employee')

        # Removing M2M table for field capabilities on 'Employee'
        db.delete_table('main_employee_capabilities')


    models = {
        u'main.capability': {
            'Meta': {'object_name': 'Capability'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'main.employee': {
            'Meta': {'object_name': 'Employee'},
            'capabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Capability']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['main']