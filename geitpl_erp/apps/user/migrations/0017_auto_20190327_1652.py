# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-27 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20190327_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tlfeedback',
            name='negative',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tlfeedback',
            name='positive',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tlfeedback',
            name='suggestion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
