# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20160131_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('poll_id', models.IntegerField()),
                ('choices', models.CharField(max_length=200)),
                ('answer_text', models.CharField(max_length=200)),
            ],
        ),
    ]