# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20170929_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('0', 'Waiting for approval'), ('1', 'Approved'), ('2', 'Cancel')], default='wa', max_length=25),
        ),
    ]
