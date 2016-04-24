# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_exam_closed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome do Aluno')),
                ('grade', models.DecimalField(decimal_places=2, default=None, max_digits=5, blank=True, null=True, verbose_name=b'Nota')),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Resposta',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alternative', models.ForeignKey(verbose_name=b'Alternativa', blank=True, to='exams.Alternative', null=True)),
                ('answer', models.ForeignKey(verbose_name=b'Resposta', to='exams.Answer')),
                ('question', models.ForeignKey(verbose_name=b'Pergunta', to='exams.Question')),
            ],
            options={
                'verbose_name': 'Uma Resposta',
                'verbose_name_plural': 'Uma Resposta',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='answers',
            field=models.ManyToManyField(to='exams.Question', verbose_name=b'Respostas', through='exams.Log'),
        ),
        migrations.AddField(
            model_name='answer',
            name='exam',
            field=models.ForeignKey(verbose_name=b'Prova', to='exams.Exam'),
        ),
    ]
