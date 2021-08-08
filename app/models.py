# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Plate(models.Model):
    COUNTRIES = [
        ('ru', 'ru'), ('am', 'am'), ('by', 'by'), ('ua', 'ua')
    ]
    name = models.CharField(max_length=30, unique=True,
        help_text='Автомобильный номер')
    country = models.CharField(max_length=20, choices=COUNTRIES, default='Ru',
        help_text='Страна')
    created = models.DateTimeField(auto_now_add=True,
        help_text='Дата создания автомобильного номера')

    def __str__(self):
        return self.name


class Grievance(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(
         help_text='Уровень возмущения от 1 до 5, где 5 - крайне возмущен!', default=3,
         validators=[
             MinValueValidator(1),
             MaxValueValidator(5)
         ])
    description = models.TextField(max_length=2000, blank=True, null=True,
        help_text='Описание')
    image = models.ImageField(blank=True, null=True,
        help_text='Фото')
    email = models.CharField(max_length=60, unique=False, blank=True, null=True,
        help_text='Email для результата')
    created = models.DateTimeField(auto_now_add=True,
        help_text='Дата создания жалобы')
    ip = models.GenericIPAddressField(blank=True, null=True)
    gibdd_id = models.CharField(max_length=30, blank=True, null=True,
        help_text='id обращения на сайте ГИБДД')
    gibdd_code = models.CharField(max_length=120, blank=True, null=True,
        help_text='Код проверки статуса обращения на сайте ГИБДД')
    gibdd_link = models.CharField(max_length=200, blank=True, null=True,
        help_text='Ссылка на обращение на сайт ГИБДД')
    result = models.CharField(max_length=2000, blank=True, null=True,
        help_text='Результат жалобы')

    def __str__(self):
        return f'{self.plate.name} at {self.created} by {self.level} level'


class Crypto(models.Model):
    name = models.CharField(max_length=128)
    fullname = models.CharField(max_length=128, blank=True, null=True)
    symbol = models.CharField(max_length=128, blank=True, null=True)
    current_price = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    highest_price = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    highest_date = models.DateTimeField(blank=True, null=True)
    limit_price = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    url = models.CharField(max_length=512)

    def __str__(self):
        return self.name
