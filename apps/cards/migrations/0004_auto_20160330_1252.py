# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20160330_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardart',
            options={'verbose_name_plural': 'card art'},
        ),
        migrations.AlterField(
            model_name='cardrevision',
            name='art',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cards.CardArt'),
        ),
    ]
