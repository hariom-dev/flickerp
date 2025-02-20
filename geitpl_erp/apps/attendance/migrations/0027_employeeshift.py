# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-07 05:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0026_auto_20180122_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_from', models.TimeField(verbose_name=b'Start time')),
                ('time_to', models.TimeField(verbose_name=b'End time')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
