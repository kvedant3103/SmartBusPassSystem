# Generated by Django 3.1.4 on 2020-12-15 08:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Vedant_Bus_app', '0019_auto_20201215_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpass',
            name='Date1',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 8, 59, 42, 471419, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='createpass',
            name='Date2',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 14, 8, 59, 42, 471419, tzinfo=utc)),
        ),
    ]