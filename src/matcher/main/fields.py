from django.db import models
from django.utils.translation import ugettext_lazy as _

class EmployeeTypeField(models.IntegerField):
    REGULAR = 1
    ALTERNATE_PUNISHMENT = 2
    TRAINEE = 3
    VOLUNTEER = 4
    choices = ((REGULAR, _("Regular")),
               (ALTERNATE_PUNISHMENT, _("Alternate punishment")),
               (TRAINEE, _("Stagiaire")),
               (VOLUNTEER, _("Volunteer")))


class DayOfTheWeekField(models.IntegerField):
    choices = ((1, _("Monday")),
          (2, _("Tuesday")),
          (3, _("Wednesday")),
          (4, _("Thursday")),
          (5, _("Friday")),
          (6,_("Saturday")))
    

class AttendanceTypeField(models.IntegerField):
    PRESENT = 1
    SPECIAL_LEAVE = 2
    SICK = 3
    UNALLOWED_LEAVE = 4
    choices = ((PRESENT, _("Present")),
               (SPECIAL_LEAVE, _("Special leave")),
               (SICK, _("Sick")),
               (UNALLOWED_LEAVE, _("Unallowed leave")))

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["matcher.main.fields.EmployeeTypeField"])
add_introspection_rules([], ["matcher.main.fields.DayOfTheWeekField"])
add_introspection_rules([], ["matcher.main.fields.AttendanceTypeField"])
