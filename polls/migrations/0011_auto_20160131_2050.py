# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160131_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpollanswer',
            name='answer_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userpollanswer',
            name='choices',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]