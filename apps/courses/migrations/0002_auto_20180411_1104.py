# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastlearn',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lastlearn',
            name='video',
        ),
        migrations.DeleteModel(
            name='LastLearn',
        ),
    ]
