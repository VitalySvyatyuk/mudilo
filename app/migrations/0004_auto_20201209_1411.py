# Generated by Django 3.1.4 on 2020-12-09 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201208_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата создания жалобы'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='description',
            field=models.TextField(blank=True, help_text='Причина', max_length=300, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='level',
            field=models.PositiveSmallIntegerField(default=3, help_text='Уровень возмущения от 1 до 5', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Уровень недовольства'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='country',
            field=models.CharField(choices=[('Ru', 'ru'), ('Am', 'am'), ('By', 'by'), ('Ua', 'ua')], default='Ru', help_text='Страна', max_length=20, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата создания номера'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='name',
            field=models.CharField(help_text='Автомобильный номер', max_length=30, unique=True, verbose_name='Автомобильный номер'),
        ),
    ]
