# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20170929_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
