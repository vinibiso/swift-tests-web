# -*- coding: utf-8 -*-
# Python
# Django
from django import forms
# Project
from .models import Exam, Question, Alternative

class ExamForm(forms.ModelForm):
    date = forms.DateField()
    class Meta:
        model = Exam
        fields = (
            "user",
            "name",
            "date"
        )

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = (
            "exam",
            "text",
        )

class AlternativeForm(forms.ModelForm):
    right = forms.BooleanField(required=False)

    class Meta:
        model = Alternative
        fields = (
            "question",
            "text",
        )

    def save(self, commit=True):
        alternative = super(AlternativeForm, self).save()
        if self.cleaned_data['right']:
            alternative.question.right_alternative = alternative
            alternative.question.save()
        return alternative
