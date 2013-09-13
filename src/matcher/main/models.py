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
    REGULAR = 1
    ALTERNATE_PUNISHMENT = 2
    TRAINEE = 3
    VOLUNTEER = 4
    CHOICES = ((REGULAR, _("Regular")),
               (ALTERNATE_PUNISHMENT, _("Alternate punishment")),
               (TRAINEE, _("Stagiaire")),
               (VOLUNTEER, _("Volunteer")))
    type = models.IntegerField(choices=CHOICES)
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
    maximum_count = models.IntegerField(_('maximum count'), default=2)
    minimum_count = models.IntegerField(_('minimum count'), default=1)
    priority = models.IntegerField(_('priority'), default=1)

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

class Attendance(models.Model):
    PRESENT = 1
    SPECIAL_LEAVE = 2
    SICK = 3
    UNALLOWED_LEAVE = 4
    CHOICES = ((PRESENT, _("Present")),
               (SPECIAL_LEAVE, _("Special leave")),
               (SICK, _("Sick")),
               (UNALLOWED_LEAVE, _("Unallowed leave")))
    type = models.IntegerField(choices=CHOICES)
    date = models.DateField(_('date'))
    checkin_time = models.TimeField(_('start time'), default=datetime.time(8, 45))
    checkout_time = models.TimeField(_('stop time'), default=datetime.time(17, 15))
    user_comment  = models.TextField(_('comment'), blank=True)

    start_time = models.TimeField(_('start time'), default=datetime.time(8, 45))
    stop_time = models.TimeField(_('stop time'), default=datetime.time(17, 15))
    task = models.ForeignKey(Task, verbose_name=_('task'))
    employee = models.ForeignKey(Employee, verbose_name=_('employee'))

    def __str__(self):
        return u"%s %s" % (self.date, self.shift)
    
