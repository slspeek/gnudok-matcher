from django.db import models
from django.utils.translation import ugettext_lazy as _

class Capability(models.Model):
    name = models.CharField(_('name'), max_length=8)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(_('name'), max_length=16)
    capabilities = models.ManyToManyField(Capability, blank=True)

    def __str__(self):
        return self.name

