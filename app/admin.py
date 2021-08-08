# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Crypto, Grievance, Plate


@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('plate', 'level', 'description', 'image', 'email',
                    'gibdd_id', 'gibdd_code', 'gibdd_link', 'created', 'ip')


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created')


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ('name', 'fullname', 'symbol', 'current_price', 'highest_price', 'highest_date',
                    'limit_price', 'url')
