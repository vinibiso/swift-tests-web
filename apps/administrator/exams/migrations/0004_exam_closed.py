# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20160423_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='closed',
            field=models.BooleanField(default=False, verbose_name=b'Fechada?'),
        ),
    ]
