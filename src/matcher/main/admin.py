'''
Admin configuration
'''
from __future__ import absolute_import
from .models import Employee, Capability, Location, Shift, Task, WorkLoad
from django.contrib import admin

class ShiftInline(admin.TabularInline):
    model = Shift

class TaskInline(admin.TabularInline):
    model = Task

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [ShiftInline,]

class LocationAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]

class WorkLoadAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Capability)
admin.site.register(Location, LocationAdmin)
admin.site.register(Shift)
admin.site.register(Task)
admin.site.register(WorkLoad)
