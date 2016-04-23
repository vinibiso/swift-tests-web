# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 4, 23, 16, 53, 17, 661855), verbose_name=b'Data'),
            preserve_default=False,
        ),
    ]
