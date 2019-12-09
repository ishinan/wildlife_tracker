# Generated by Django 3.0 on 2019-12-08 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='lat_position',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='lon_position',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='submitted_images/'),
        ),
    ]
