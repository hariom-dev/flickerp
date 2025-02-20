# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-12-01 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20190311_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('open', 'Working'), ('expected', 'Expected to Start'), ('scheduled', 'Scheduled to Start'), ('pause', 'paused'), ('closed', 'closed'), ('expire', 'expired'), ('done', 'complted')], max_length=30, verbose_name='Services Status'),
        ),
        migrations.AlterField(
            model_name='servicerecords',
            name='status',
            field=models.CharField(choices=[('open', 'Working'), ('expected', 'Expected to Start'), ('scheduled', 'Scheduled to Start'), ('pause', 'paused'), ('closed', 'closed'), ('expire', 'expired'), ('done', 'complted')], default='open', max_length=30, verbose_name='Services Status'),
        ),
    ]
