'''
Admin configuration
'''
from __future__ import absolute_import
from .models import Employee, Capability
from django.contrib import admin


admin.site.register(Employee)
admin.site.register(Capability)
