from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
import datetime
from .fields import EmployeeTypeField, DayOfTheWeekField, AttendanceTypeField

class Capability(models.Model):
    name = models.CharField(_('name'), max_length=20)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    type = EmployeeTypeField(_('type'))
    parent = models.OneToOneField(User, verbose_name=_('user'))
    capabilities = models.ManyToManyField(Capability, blank=True)
    address = models.CharField(_('address'), max_length=30)
    town = models.CharField(_('town'), max_length=20)
    telephone = models.CharField(_('telephone'), max_length=20)
    emergency = models.TextField(_('emergency'), blank=True)

    def __str__(self):
        return self.parent.get_full_name()


class Contract(models.Model):
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))
    employee = models.ForeignKey(Employee, verbose_name=('employee'))
    contact_data = models.TextField(_('contact data'), blank=True)


class Location(models.Model):
    name = models.CharField(_('name'), max_length=20)
    description =  models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(_('name'), max_length=20)
    description =  models.TextField(_('description'), blank=True)
    location = models.ForeignKey(Location, verbose_name=_('location'))
    capability = models.ForeignKey(Capability, verbose_name=('capability'), blank=True)
    minimum_count = models.IntegerField(_('minimum count'), default=1)
    maximum_count = models.IntegerField(_('maximum count'), default=2)
    priority = models.IntegerField(_('priority'), default=1)

    def __str__(self):
        return u"%s %s %s" % (self.name, _('at'), self.location)


class TaskShift(models.Model):
    day_of_week = DayOfTheWeekField(_('day of the week'))
    start_time = models.TimeField(_('start time'), default=datetime.time(8, 45))
    stop_time = models.TimeField(_('stop time'), default=datetime.time(17, 15))
    task = models.ForeignKey(Task, verbose_name=_('task'))

    def __str__(self):
        return u"%s %s :  %s - %s" % (self.task,
                                      self.get_day_of_week_display(),
                                      self.start_time,
                                      self.stop_time)

class Shift(models.Model):
    day_of_week = DayOfTheWeekField(_('day of the week'))
    start_time = models.TimeField(_('start time'), default=datetime.time(8, 45))
    stop_time = models.TimeField(_('stop time'), default=datetime.time(17, 15))
    task = models.ForeignKey(Task, verbose_name=_('task'))
    employee = models.ForeignKey(Employee, verbose_name=_('employee'))

    def __str__(self):
        return u"%s %s %s :  %s - %s" % (self.employee, 
                                      self.task,
                                      self.get_day_of_week_display(),
                                      self.start_time,
                                      self.stop_time)

class Attendance(models.Model):
    type = AttendanceTypeField(_('type'))
    date = models.DateField(_('date'))
    checkin_time = models.TimeField(_('checkin time'))
    checkout_time = models.TimeField(_('checkout time'))
    user_comment  = models.TextField(_('comment'), blank=True)

    start_time = models.TimeField(_('start time'))
    stop_time = models.TimeField(_('stop time'))
    task = models.ForeignKey(Task, verbose_name=_('task'))
    employee = models.ForeignKey(Employee, verbose_name=_('employee'))

    def __str__(self):
        return u"%s %s %s" % (self.date, self.type, self.employee)
    
