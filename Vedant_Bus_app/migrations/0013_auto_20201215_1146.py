# Generated by Django 3.1.4 on 2020-12-15 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vedant_Bus_app', '0012_auto_20201215_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpass',
            name='Date2',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 11, 46, 35, 768972)),
        ),
        migrations.AlterField(
            model_name='createpass',
            name='expiry',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='renewpass',
            name='Date2',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 11, 46, 35, 768972)),
        ),
    ]