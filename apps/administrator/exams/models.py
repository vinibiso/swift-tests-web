# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Exam(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuário")
    name = models.CharField(max_length=100, verbose_name="Nome")
    date = models.DateField(verbose_name="Data")
    active = models.BooleanField(default=False, verbose_name="Ativo?")
    closed = models.BooleanField(default=False, verbose_name="Fechada?")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Prova"
        verbose_name_plural = "Provas"

    def get_absolute_url(self):
        return reverse('exam_update', kwargs={'exam': self.pk})

class Question(models.Model):
    exam = models.ForeignKey(Exam, verbose_name="Prova")
    text = models.CharField(max_length=100, verbose_name="Texto")
    right_alternative = models.ForeignKey("Alternative", related_name="question_right_alternative", blank=True, null=True, default=None)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'exam': self.exam.pk, 'pk': self.pk})

class Alternative(models.Model):
    question = models.ForeignKey(Question, verbose_name="Questão")
    text = models.CharField(max_length=100, verbose_name="Texto")

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'exam': self.question.exam.pk, 'pk': self.question.pk})

    def delete(self):
        if self.question.right_alternative == self:
            self.question.right_alternative = None
            self.question.save()
        super(Alternative, self).delete()
