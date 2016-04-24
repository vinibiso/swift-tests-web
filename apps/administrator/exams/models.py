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
        return reverse('exam_detail', kwargs={'exam': self.pk})

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

class Answer(models.Model):
    exam = models.ForeignKey(Exam, verbose_name="Prova")
    name = models.CharField(max_length=100, verbose_name="Nome do Aluno")
    grade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nota", blank=True, null=True, default=None)
    answers = models.ManyToManyField(Question, through="Log", verbose_name="Respostas")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Data Recebida")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Resposta"

class Log(models.Model):
    answer = models.ForeignKey(Answer, verbose_name="Resposta")
    question = models.ForeignKey(Question, verbose_name="Pergunta")
    alternative = models.ForeignKey(Alternative, blank=True, null=True, verbose_name="Alternativa")

    def __unicode__(self):
        return self.answer.name

    class Meta:
        verbose_name = "Uma Resposta"
        verbose_name_plural = "Uma Resposta"
