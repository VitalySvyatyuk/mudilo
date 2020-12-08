# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _


class Plate(models.Model):
    COUNTRIES = [
        ('Ru', 'ru'), ('Am', 'am'), ('By', 'by'), ('Ua', 'ua')
    ]
    name = models.CharField(_('License Plate'), max_length=30,
        help_text=_('License plate of the vehicle'))
    country = models.CharField(_('Country'), max_length=20, choices=COUNTRIES, default='ru',
        help_text=_('Country'))
    created = models.DateTimeField(auto_now_add=True,
        help_text=_('Plate creation date'))

    def __str__(self):
        return self.name


class Grievance(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(_('Anger Level'),
         help_text=_('The level of discontent from 1 to 5'), default=3,
         validators=[
             MaxValueValidator(5),
             MinValueValidator(1)
         ])
    description = models.TextField(_('Description'), max_length=300, blank=True, null=True,
        help_text=_('The reason of the grievance'),)
    created = models.DateTimeField(auto_now_add=True,
        help_text=_('Grievance creation date'))

    def __str__(self):
        return f'{self.plate.name} at {self.created} by {self.level} level'
