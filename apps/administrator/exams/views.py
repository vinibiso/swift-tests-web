# -*- coding: utf-8 -*-
# Python
# Django
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Project
from apps.api.useful import make_response
# Models
from django.contrib.auth.models import User
from .models import Exam, Question, Alternative, Answer, Log
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

class ExamNotActiveOrClosedMixin(object):
    def dispatch(self, *args, **kwargs):
        exam = get_object_or_404(Exam, pk=kwargs['exam'])
        if exam.active or exam.closed:
            messages.add_message(self.request, messages.ERROR, 'exam_active_or_closed')
            return redirect('exam_detail', exam = exam.pk)
        return super(ExamNotActiveOrClosedMixin, self).dispatch(*args, **kwargs)

class DeleteSucessMessageMixing(object):
    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, self.success_message)
        return super(DeleteSucessMessageMixing, self).delete(request, *args, **kwargs)

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
class ExamUpdate(SuccessMessageMixin, ExamNotActiveOrClosedMixin, LoginRequiredMixin, UsersExamMixin, UpdateView):
    template_name = 'exam/exam_form.html'
    model = Exam
    form_class = ExamForm
    success_message = 'update_success'

    def get_object(self):
        exam = get_object_or_404(Exam, pk=self.kwargs['exam'])
        return exam

# View that controls the delete of a Question
class ExamDelete(DeleteSucessMessageMixing, ExamNotActiveOrClosedMixin, LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = 'exam/exam_delete.html'
    success_url = reverse_lazy('exam_list')
    success_message = 'exam_delete_success'

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
class QuestionUpdate(SuccessMessageMixin, ExamNotActiveOrClosedMixin, UsersExamMixin, LoginRequiredMixin, ExamToContextMixin, UpdateView):
    template_name = 'question/question_form.html'
    model = Question
    form_class = QuestionForm
    success_message = 'question_update_success'

# View that controls the delete of a Question
class QuestionDelete(DeleteSucessMessageMixing, ExamNotActiveOrClosedMixin, LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'question/question_delete.html'
    success_url = ''
    success_message = 'question_delete_success'

    def get_success_url(self):
        return reverse('exam_detail', kwargs={'exam': self.object.exam.pk })

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
class AlternativeUpdate(SuccessMessageMixin, ExamNotActiveOrClosedMixin, UsersExamMixin, LoginRequiredMixin, ExamToContextMixin, QuestionToContextMixin, UpdateView):
    template_name = 'alternative/alternative_form.html'
    model = Alternative
    form_class = AlternativeForm
    success_message = 'alternative_update_success'

# View that controls the delete of a Alternative
class AlternativeDelete(DeleteSucessMessageMixing, ExamNotActiveOrClosedMixin, LoginRequiredMixin, DeleteView):
    model = Alternative
    template_name = 'alternative/alternative_delete.html'
    success_url = ''
    success_message = 'alternative_delete_success'

    def get_success_url(self):
        return reverse('question_detail', kwargs={'exam': self.object.question.exam.pk, 'pk': self.object.question.pk})

# View that activates a test to be synchronized
class ExamActivateView(UsersExamMixin, LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        exam = get_object_or_404(Exam.objects.filter(active=False, closed=False), pk=kwargs['exam'])
        Exam.objects.filter(active=True, closed=False).update(active=False, closed=True)
        for question in exam.question_set.all():
            if question.right_alternative == None:
                messages.add_message(request, messages.ERROR, 'answers_not_in')
                return redirect('exam_detail', exam = exam.pk)
        exam.active = True
        exam.save()
        messages.add_message(request, messages.SUCCESS, 'exam_activated')
        return redirect('exam_report', exam = exam.pk)

# View that closes a test to be synchronized
class ExamCloseView(UsersExamMixin, LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        exam = get_object_or_404(Exam.objects.filter(active=True, closed=False), pk=kwargs['exam'])
        exam.active = False
        exam.closed = True
        exam.save()
        messages.add_message(request, messages.SUCCESS, 'exam_closed')
        return redirect('exam_detail', exam = exam.pk)

# Shows Exam Report
class ExamReport(LoginRequiredMixin, UsersExamMixin, DetailView):
    template_name = 'exam/exam_report.html'
    model = Exam

    def get_object(self):
        exam = get_object_or_404(Exam, pk=self.kwargs['exam'])
        return exam

# Shows Exam Report
class ExamReportData(LoginRequiredMixin, UsersExamMixin, DetailView):
    template_name = ""
    model = Exam

    def get_object(self):
        exam = get_object_or_404(Exam, pk=self.kwargs['exam'])
        return exam

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        answers = self.object.answer_set.all().order_by('id')
        response = serialize_answers(answers)
        return make_response(response)

def serialize_answers(answers):
    new_answers = []
    for a in answers:
        new_answer = {
            "name": a.name,
            "grade": None if a.grade == None else float(a.grade),
            "date": str(a.date),
            "logs": []
        }
        for l in Log.objects.filter(answer = a).order_by("question__id"):
            new_log = {
                "question_id": l.question.id,
                "question": l.question.text,
                "alternative_id": None if l.alternative == None else l.alternative.id,
                "alternative": "-" if l.alternative == None else l.alternative.text
            }
            new_answer['logs'].append(new_log)

        new_answers.append(new_answer)
    return new_answers
