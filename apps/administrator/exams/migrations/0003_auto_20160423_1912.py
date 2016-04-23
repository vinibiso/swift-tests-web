# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_exam_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternative',
            name='right',
        ),
        migrations.AddField(
            model_name='question',
            name='right_alternative',
            field=models.ForeignKey(related_name='question_right_alternative', default=None, blank=True, to='exams.Alternative', null=True),
        ),
    ]
