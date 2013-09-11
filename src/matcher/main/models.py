from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
import datetime

class Capability(models.Model):
    name = models.CharField(_('name'), max_length=20)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    parent = models.OneToOneField(User, verbose_name=_('user'))
    capabilities = models.ManyToManyField(Capability, blank=True)

    def __str__(self):
        return self.parent.get_full_name()


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

    def __str__(self):
        return u"%s %s %s" % (self.name, _('at'), self.location)


class Shift(models.Model):
    CHOICES = ((1, _("Monday")),
               (2, _("Tuesday")),
               (3, _("Wednesday")),
               (4, _("Thursday")),
               (5, _("Friday")),
               (6,_("Saturday")))
    day_of_week = models.IntegerField(choices=CHOICES)
    start_time = models.TimeField(_('start time'), default=datetime.time(8, 45))
    stop_time = models.TimeField(_('stop time'), default=datetime.time(17, 15))
    task = models.ForeignKey(Task, verbose_name=_('task'))
    employee = models.ForeignKey(Employee, verbose_name=_('employee'))

    def __str__(self):
        return u"%s %s :  %s - %s" % (self.task,
                                   self.get_day_of_week_display(),
                                   self.start_time,
                                   self.stop_time)

class WorkLoad(models.Model):
    date = models.DateField(_('date'))
    shift = models.ForeignKey(Shift, verbose_name=_('shift'))
    start_time = models.TimeField(_('start time'), default=datetime.time(8, 45))
    stop_time = models.TimeField(_('stop time'), default=datetime.time(17, 15))
    user_comment  = models.TextField(_('Comment'), blank=True)
    
