# Generated by Django 3.0 on 2019-12-13 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191213_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='sighting_time',
        ),
    ]
