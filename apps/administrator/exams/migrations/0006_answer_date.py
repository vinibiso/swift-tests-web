# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20160424_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 24, 15, 54, 23, 276564), verbose_name=b'Data Recebida', auto_now_add=True),
            preserve_default=False,
        ),
    ]
