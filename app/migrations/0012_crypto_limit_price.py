# Generated by Django 3.1.4 on 2021-08-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_crypto'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='limit_price',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=30),
        ),
    ]
