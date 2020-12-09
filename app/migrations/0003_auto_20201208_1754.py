# Generated by Django 3.1.4 on 2020-12-08 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_plate_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Grievance creation date'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='description',
            field=models.TextField(blank=True, help_text='The reason of the grievance', max_length=300, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='level',
            field=models.PositiveSmallIntegerField(default=3, help_text='The level of discontent from 1 to 5', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Уровень злости.'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='country',
            field=models.CharField(choices=[('Ru', 'ru'), ('Am', 'am'), ('By', 'by'), ('Ua', 'ua')], default='ru', help_text='Country', max_length=20, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Plate creation date'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='name',
            field=models.CharField(help_text='License plate of the vehicle', max_length=30, verbose_name='Автомобильный номер'),
        ),
    ]