# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Grievance, Plate

from django.contrib import admin


@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('plate', 'level', 'description', 'image', 'email',
                    'gibdd_id', 'gibdd_code', 'gibdd_link', 'created', 'ip')


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created')
