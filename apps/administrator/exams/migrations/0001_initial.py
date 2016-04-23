# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100, verbose_name=b'Texto')),
                ('right', models.BooleanField(default=False, verbose_name=b'Certa?')),
            ],
            options={
                'verbose_name': 'Alternativa',
                'verbose_name_plural': 'Alternativas',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('active', models.BooleanField(default=False, verbose_name=b'Ativo?')),
                ('user', models.ForeignKey(verbose_name=b'Usu\xc3\xa1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Prova',
                'verbose_name_plural': 'Provas',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100, verbose_name=b'Texto')),
                ('exam', models.ForeignKey(verbose_name=b'Prova', to='exams.Exam')),
            ],
            options={
                'verbose_name': 'Quest\xe3o',
                'verbose_name_plural': 'Quest\xf5es',
            },
        ),
        migrations.AddField(
            model_name='alternative',
            name='question',
            field=models.ForeignKey(verbose_name=b'Quest\xc3\xa3o', to='exams.Question'),
        ),
    ]
