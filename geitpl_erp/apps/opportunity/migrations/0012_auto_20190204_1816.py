# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-04 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0011_auto_20190204_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opportunity',
            old_name='conatct',
            new_name='contact',
        ),
    ]
