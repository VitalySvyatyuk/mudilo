# Generated by Django 3.1.4 on 2021-01-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201226_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='description',
            field=models.TextField(blank=True, help_text='Описание ситуации', max_length=500, null=True, verbose_name='Описание'),
        ),
    ]