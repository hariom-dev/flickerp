# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-04 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0012_auto_20190204_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='looking_for_hire',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='technology',
        ),
    ]
