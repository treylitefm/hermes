# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20160929_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='screenshot_url',
            new_name='screenshot',
        ),
    ]
