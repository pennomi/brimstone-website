# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 04:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20160408_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardrevision',
            name='table',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[]),
        ),
        migrations.AddField(
            model_name='cardrevision',
            name='table_y',
            field=models.IntegerField(default=0),
        ),
    ]
