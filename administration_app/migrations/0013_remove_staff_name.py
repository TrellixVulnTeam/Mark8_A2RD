# Generated by Django 2.0.5 on 2018-05-20 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration_app', '0012_auto_20180518_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
    ]
