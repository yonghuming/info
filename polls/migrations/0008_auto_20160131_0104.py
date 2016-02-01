# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160130_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=b'1', max_length=200, choices=[(b'1', b'\xe5\x8d\x95\xe9\x80\x89\xe9\xa2\x98'), (b'2', b'\xe5\xa4\x9a\xe9\x80\x89\xe9\xa2\x98'), (b'3', b'\xe5\xa1\xab\xe7\xa9\xba\xe9\xa2\x98'), (b'4', b'\xe7\xae\x80\xe7\xad\x94\xe9\xa2\x98')]),
        ),
    ]
