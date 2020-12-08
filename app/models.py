# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _


class Plate(models.Model):
    name = models.CharField(_('License Plate'), max_length=30, help_text=_('License plate of the vehicle.'))
    created = models.DateTimeField(auto_now_add=True, help_text=_('Plate creation date.'))

    def __str__(self):
        return self.name


class Grievance(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(_('Anger Level'), help_text=_('The level of discontent. From 1 to 5.'), default=3,
                                             validators=[
                                                 MaxValueValidator(5),
                                                 MinValueValidator(1)
                                             ])
    description = models.TextField(help_text=_('The reason of the grievance.'), max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, help_text=_('Grievance creation date.'))

    def __str__(self):
        return f'{self.plate.name} at {self.created} by {self.level} level'
