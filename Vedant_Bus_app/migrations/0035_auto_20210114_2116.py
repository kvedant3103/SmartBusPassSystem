# Generated by Django 3.1.4 on 2021-01-14 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vedant_Bus_app', '0034_auto_20210114_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpass',
            name='Date1',
            field=models.CharField(default=datetime.datetime(2021, 1, 14, 21, 16, 58, 163031), max_length=50, null=True),
        ),
    ]
