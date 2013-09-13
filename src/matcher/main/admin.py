'''
Admin configuration
'''
from __future__ import absolute_import
from .models import Employee, Capability, Location, Shift, Task, TaskShift,  Attendance
from django.contrib import admin

class ShiftInline(admin.TabularInline):
    model = Shift

class TaskInline(admin.TabularInline):
    model = Task

class TaskShiftInline(admin.TabularInline):
    model = TaskShift

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [ShiftInline,]

class LocationAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]

class AttendanceAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'

class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskShiftInline,]
    
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Capability)
admin.site.register(Location, LocationAdmin)
admin.site.register(Shift)
admin.site.register(Task, TaskAdmin)
admin.site.register(Attendance, AttendanceAdmin)
