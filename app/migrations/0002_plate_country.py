# Generated by Django 3.1.4 on 2020-12-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='country',
            field=models.CharField(choices=[('Ru', 'ru'), ('Am', 'am'), ('By', 'by'), ('Ua', 'ua')], default='ru', help_text='Country.', max_length=20),
        ),
    ]
