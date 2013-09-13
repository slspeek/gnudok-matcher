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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'main', ['Capability'])

        # Adding model 'Employee'
        db.create_table(u'main_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('matcher.main.fields.EmployeeTypeField')()),
            ('parent', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('emergency', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'main', ['Employee'])

        # Adding M2M table for field capabilities on 'Employee'
        m2m_table_name = db.shorten_name(u'main_employee_capabilities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employee', models.ForeignKey(orm[u'main.employee'], null=False)),
            ('capability', models.ForeignKey(orm[u'main.capability'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employee_id', 'capability_id'])

        # Adding model 'Contract'
        db.create_table(u'main_contract', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Employee'])),
            ('contact_data', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'main', ['Contract'])

        # Adding model 'Location'
        db.create_table(u'main_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'main', ['Location'])

        # Adding model 'Task'
        db.create_table(u'main_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Location'])),
            ('capability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Capability'], blank=True)),
            ('minimum_count', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('maximum_count', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'main', ['Task'])

        # Adding model 'TaskShift'
        db.create_table(u'main_taskshift', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day_of_week', self.gf('matcher.main.fields.DayOfTheWeekField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')(default=datetime.time(8, 45))),
            ('stop_time', self.gf('django.db.models.fields.TimeField')(default=datetime.time(17, 15))),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Task'])),
        ))
        db.send_create_signal(u'main', ['TaskShift'])

        # Adding model 'Shift'
        db.create_table(u'main_shift', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day_of_week', self.gf('matcher.main.fields.DayOfTheWeekField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')(default=datetime.time(8, 45))),
            ('stop_time', self.gf('django.db.models.fields.TimeField')(default=datetime.time(17, 15))),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Task'])),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Employee'])),
        ))
        db.send_create_signal(u'main', ['Shift'])

        # Adding model 'Attendance'
        db.create_table(u'main_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('matcher.main.fields.AttendanceTypeField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('checkin_time', self.gf('django.db.models.fields.TimeField')()),
            ('checkout_time', self.gf('django.db.models.fields.TimeField')()),
            ('user_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('stop_time', self.gf('django.db.models.fields.TimeField')()),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Task'])),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Employee'])),
        ))
        db.send_create_signal(u'main', ['Attendance'])


    def backwards(self, orm):
        # Deleting model 'Capability'
        db.delete_table(u'main_capability')

        # Deleting model 'Employee'
        db.delete_table(u'main_employee')

        # Removing M2M table for field capabilities on 'Employee'
        db.delete_table(db.shorten_name(u'main_employee_capabilities'))

        # Deleting model 'Contract'
        db.delete_table(u'main_contract')

        # Deleting model 'Location'
        db.delete_table(u'main_location')

        # Deleting model 'Task'
        db.delete_table(u'main_task')

        # Deleting model 'TaskShift'
        db.delete_table(u'main_taskshift')

        # Deleting model 'Shift'
        db.delete_table(u'main_shift')

        # Deleting model 'Attendance'
        db.delete_table(u'main_attendance')


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
        u'main.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'checkin_time': ('django.db.models.fields.TimeField', [], {}),
            'checkout_time': ('django.db.models.fields.TimeField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'stop_time': ('django.db.models.fields.TimeField', [], {}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Task']"}),
            'type': ('matcher.main.fields.AttendanceTypeField', [], {}),
            'user_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'main.capability': {
            'Meta': {'object_name': 'Capability'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.contract': {
            'Meta': {'object_name': 'Contract'},
            'contact_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Employee']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'main.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'capabilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Capability']", 'symmetrical': 'False', 'blank': 'True'}),
            'emergency': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('matcher.main.fields.EmployeeTypeField', [], {})
        },
        u'main.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.shift': {
            'Meta': {'object_name': 'Shift'},
            'day_of_week': ('matcher.main.fields.DayOfTheWeekField', [], {}),
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
            'maximum_count': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'minimum_count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'main.taskshift': {
            'Meta': {'object_name': 'TaskShift'},
            'day_of_week': ('matcher.main.fields.DayOfTheWeekField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(8, 45)'}),
            'stop_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(17, 15)'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Task']"})
        }
    }

    complete_apps = ['main']