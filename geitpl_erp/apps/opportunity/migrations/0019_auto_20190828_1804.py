# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-08-28 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0018_auto_20190704_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(choices=[(b'1', b'Website'), (b'2', b'Email Marketing'), (b'3', b'Client Reference'), (b'4', b'Linkedin'), (b'5', b'Facebook'), (b'6', b'Whatsapp'), (b'7', b'Clutch'), (b'8', b'Craigslist'), (b'9', b'Other')], default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[(b'1', b'New'), (b'2', b'Positive Response'), (b'3', b'Hot Prospect'), (b'4', b'converted to Project'), (b'5', b'Not Intrested'), (b'6', b'No Response'), (b'111', b'Created by Website')], default=b'1', max_length=4),
        ),
        migrations.AlterField(
            model_name='leadscheduler',
            name='call_schedule',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Next schedule Date if any'),
        ),
        migrations.AlterField(
            model_name='leadscheduler',
            name='communication_type',
            field=models.CharField(choices=[(b'1', b'Skype'), (b'2', b'Drop a Email'), (b'3', b'Phone Call'), (b'4', b'Linkedin'), (b'5', b'Facebook'), (b'6', b'Whatsapp'), (b'7', b'Other')], max_length=20, verbose_name=b'Mediam of communication'),
        ),
        migrations.AlterField(
            model_name='leadscheduler',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name=b'Client communication Details'),
        ),
        migrations.AlterField(
            model_name='leadscheduler',
            name='result',
            field=models.CharField(choices=[(b'0', b'Mark as Lead'), (b'1', b'Next call'), (b'2', b'Lose'), (b'3', b'No Response'), (b'4', b'complted')], default=b'1', max_length=1, verbose_name=b'Result of Last call'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.TextField(blank=True, help_text=b'its can be project or client detail', null=True, verbose_name=b'Project Details'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='firstname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='source',
            field=models.CharField(choices=[(b'1', b'Website'), (b'2', b'Email Marketing'), (b'3', b'Client Reference'), (b'4', b'Linkedin'), (b'5', b'Facebook'), (b'6', b'Whatsapp'), (b'7', b'Clutch'), (b'8', b'Craigslist'), (b'9', b'Other')], default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='status',
            field=models.CharField(choices=[(b'1', b'New'), (b'2', b'Positive Response'), (b'3', b'Hot Prospect'), (b'4', b'converted to Lead'), (b'5', b'Not Intrested'), (b'6', b'No Response'), (b'111', b'Created by Website')], default=b'1', max_length=4),
        ),
        migrations.AlterField(
            model_name='opportunityscheduler',
            name='call_schedule',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Next schedule Date if any'),
        ),
        migrations.AlterField(
            model_name='opportunityscheduler',
            name='communication_type',
            field=models.CharField(choices=[(b'1', b'Skype'), (b'2', b'Drop a Email'), (b'3', b'Phone Call'), (b'4', b'Linkedin'), (b'5', b'Facebook'), (b'6', b'Whatsapp'), (b'7', b'Other')], max_length=20, verbose_name=b'Mediam of communication'),
        ),
        migrations.AlterField(
            model_name='opportunityscheduler',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name=b'Client communication Details'),
        ),
        migrations.AlterField(
            model_name='opportunityscheduler',
            name='result',
            field=models.CharField(choices=[(b'0', b'Mark as Lead'), (b'1', b'Next call'), (b'2', b'Lose'), (b'3', b'No Response'), (b'4', b'complted')], default=b'1', max_length=1, verbose_name=b'Result of Last call'),
        ),
    ]
