# Generated by Django 3.1.4 on 2021-05-26 09:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210526_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='image',
            field=models.ImageField(blank=True, help_text='Фото', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='description',
            field=models.TextField(blank=True, help_text='Описание', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='email',
            field=models.CharField(blank=True, help_text='Email для результата', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='gibdd_code',
            field=models.CharField(blank=True, help_text='Код проверки статуса обращения на сайте ГИБДД', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='gibdd_id',
            field=models.CharField(blank=True, help_text='id обращения на сайте ГИБДД', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='gibdd_link',
            field=models.CharField(blank=True, help_text='Ссылка на обращение на сайт ГИБДД', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='level',
            field=models.PositiveSmallIntegerField(default=3, help_text='Уровень возмущения от 1 до 5, где 5 - крайне возмущен!', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='result',
            field=models.CharField(blank=True, help_text='Результат жалобы', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='plate',
            name='country',
            field=models.CharField(choices=[('ru', 'ru'), ('am', 'am'), ('by', 'by'), ('ua', 'ua')], default='Ru', help_text='Страна', max_length=20),
        ),
        migrations.AlterField(
            model_name='plate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата создания автомобильного номера'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='name',
            field=models.CharField(help_text='Автомобильный номер', max_length=30, unique=True),
        ),
    ]