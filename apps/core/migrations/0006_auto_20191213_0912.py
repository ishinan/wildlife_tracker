# Generated by Django 3.0 on 2019-12-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191213_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='text',
        ),
        migrations.AddField(
            model_name='report',
            name='detailed_description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='animal_type',
            field=models.CharField(choices=[('BEAR', 'Bear'), ('BOBCAT', 'Bobcat'), ('CAT', 'Cat'), ('COYOTEE', 'Coyotee'), ('DEER', 'Deer'), ('EAGLE', 'Eagle'), ('EL CHUPACABRA', 'El Chupacabra'), ('MOUNTAIN LION', 'Mountain Lion'), ('WOLF', 'Wolf'), ('OTHER', 'Other')], default='COYOTEE', max_length=20),
        ),
    ]
