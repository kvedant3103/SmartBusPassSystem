# Generated by Django 3.1.4 on 2020-12-13 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vedant_Bus_app', '0004_createpass_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createpass',
            name='qr_codes',
        ),
    ]
