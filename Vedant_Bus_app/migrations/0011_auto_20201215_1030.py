# Generated by Django 3.1.4 on 2020-12-15 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vedant_Bus_app', '0010_auto_20201215_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpass',
            name='Date2',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 10, 30, 32, 545278)),
        ),
    ]