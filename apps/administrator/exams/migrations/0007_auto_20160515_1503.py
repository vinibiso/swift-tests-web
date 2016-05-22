# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_answer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='right_alternative',
            field=models.OneToOneField(related_name='question_right_alternative', null=True, default=None, blank=True, to='exams.Alternative'),
        ),
    ]
