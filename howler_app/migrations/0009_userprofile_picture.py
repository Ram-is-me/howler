# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howler_app', '0008_userprofile_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='user_profiles'),
        ),
    ]
