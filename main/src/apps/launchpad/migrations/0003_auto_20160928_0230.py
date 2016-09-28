# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchpad', '0002_app_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AddField(
            model_name='app',
            name='domain',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='app',
            name='protocol',
            field=models.CharField(choices=[(0, 'http'), (1, 'https')], default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='page',
            name='path',
            field=models.CharField(default='/', max_length=255),
        ),
    ]