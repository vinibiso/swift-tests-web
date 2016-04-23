# -*- coding: utf-8 -*-
# Python
# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Project
# Models
from django.contrib.auth.models import User
from .models import Exam, Question, Alternative
# Forms
from .forms import ExamForm, QuestionForm, AlternativeForm
# Mixins
from apps.administrator.main.mixins import LoginRequiredMixin

# Create your views here.
class UsersExamMixin(object):
    def dispatch(self, *args, **kwargs):
        exam = get_object_or_404(Exam, pk=kwargs['exam'])
        if exam.user != self.request.user:
            return redirect('login')
        return super(UsersExamMixin, self).dispatch(*args, **kwargs)

class ExamToContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ExamToContextMixin, self).get_context_data(**kwargs)
        context['exam'] = get_object_or_404(Exam, pk=self.kwargs['exam'])
        return context

# Lists all exams orderd by date and paginated
class ExamList(LoginRequiredMixin, ListView):
    template_name = 'exam/exam_list.html'
    queryset = Exam.objects.all().order_by('date')
    paginate_by = 10

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)


# Shows Exam details
class ExamDetail(LoginRequiredMixin, UsersExamMixin, DetailView):
    template_name = 'exam/exam_detail.html'
    model = Exam

    def get_object(self):
        exam = get_object_or_404(Exam, pk=self.kwargs['exam'])
        return exam

    def get_context_data(self, **kwargs):
        context = super(ExamDetail, self).get_context_data(**kwargs)
        context['questions'] = self.object.question_set.all().order_by('id')
        return context

# Controls behavior to create a new Exam
class ExamCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'exam/exam_form.html'
    model = Exam
    form_class = ExamForm
    success_message = 'create_success'

# Controls behavior to update a Exam
class ExamUpdate(SuccessMessageMixin, LoginRequiredMixin, UsersExamMixin, UpdateView):
    template_name = 'exam/exam_form.html'
    model = Exam
    form_class = ExamForm
    success_message = 'update_success'

    def get_object(self):
        exam = get_object_or_404(Exam, pk=self.kwargs['exam'])
        return exam

# Shows Question details
class QuestionDetail(LoginRequiredMixin, UsersExamMixin, ExamToContextMixin, DetailView):
    template_name = 'question/question_detail.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['alternatives'] = self.object.alternative_set.all().order_by('id')
        return context

# Controls behavior to create a new Question
class QuestionCreate(SuccessMessageMixin, UsersExamMixin, LoginRequiredMixin, ExamToContextMixin, CreateView):
    template_name = 'question/question_form.html'
    model = Question
    form_class = QuestionForm
    success_message = 'question_create_success'

# Controls behavior to update a Exam
class QuestionUpdate(SuccessMessageMixin, UsersExamMixin, LoginRequiredMixin, ExamToContextMixin, UpdateView):
    template_name = 'question/question_form.html'
    model = Question
    form_class = QuestionForm
    success_message = 'question_update_success'


class QuestionToContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(QuestionToContextMixin, self).get_context_data(**kwargs)
        context['question'] = get_object_or_404(Question, pk=self.kwargs['question'])
        return context

# Controls behavior to create a new Question
class AlternativeCreate(SuccessMessageMixin, UsersExamMixin, LoginRequiredMixin, ExamToContextMixin, QuestionToContextMixin, CreateView):
    template_name = 'alternative/alternative_form.html'
    model = Alternative
    form_class = AlternativeForm
    success_message = 'alternative_create_success'

# Controls behavior to update a Exam
class AlternativeUpdate(SuccessMessageMixin, UsersExamMixin, LoginRequiredMixin, ExamToContextMixin, QuestionToContextMixin, UpdateView):
    template_name = 'alternative/alternative_form.html'
    model = Alternative
    form_class = AlternativeForm
    success_message = 'alternative_update_success'
