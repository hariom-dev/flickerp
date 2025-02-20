# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180105_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheettype',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='timesheettype',
            name='field_type',
            field=models.CharField(choices=[('user', 'User Model'), ('service', 'Service Model'), ('text', 'Text filed'), ('m2m_user', 'Many to Many User'), ('m2m_service', 'Many to Many User')], default='text', max_length=100, verbose_name='Timesheet Type'),
        ),
    ]
