# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-22 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20180112_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='designation',
            field=models.CharField(blank=True, choices=[(b'trainee', b'Trainee'), (b'jr_developer', b'Jr. Developer'), (b'developer', b'Developer'), (b'sr_developer', b'Sr. Developer'), (b'atl', b'Asst. Team Lead'), (b'tl', b'Team Lead'), (b'apm', b'Asst Project Manager'), (b'pm', b'Project Manager'), (b'fd', b'Front Desk'), (b'SEO', b'Chief Executive officer'), (b'CTO', b'Chief Technical officer'), (b'BDE', b'Business Development Executive'), (b'seo_executive', b'Seo Executive'), (b'sr_seo_executive', b'Sr seo executive'), (b'jr_seo_executive', b'Jr seo executive')], max_length=100, null=True),
        ),
    ]
