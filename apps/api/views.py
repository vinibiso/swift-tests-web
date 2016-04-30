# Python
import json
import traceback
# Django
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
# Project
from apps.administrator.exams.models import Exam, Question, Alternative, Answer, Log
# Module
from .mixins import NoCSRFMixin
from .useful import make_response

# Ping API
class Ping(NoCSRFMixin, View):
    def post(self, request, *args, **kwargs):
        if settings.API_ON:
            return make_response({"message": "UP"})
        return make_response({"message": "DOWN"})

    def get(self, request, *args, **kwargs):
        if settings.API_ON:
            return make_response({"message": "UP"})
        return make_response({"message": "DOWN"})

# Returns a new EXAM one is active
class SendExamView(NoCSRFMixin, View):
    def post(self, request, *args, **kwargs):
        response = {"message": "NO_TEST"}
        exams = Exam.objects.filter(active=True, closed=False).order_by("id")
        if exams.count() > 0:
            exam = exams[0]
            response["message"] = "TEST"
            response["exam"] = serialize_exam(exam)
        return make_response(response)

# Receives a new answer to an Exam
class ReceiveVoteView(NoCSRFMixin, View):
    def post(self, request, *args, **kwargs):
        response = {"message": "OK"}
        answer = json.loads(request.POST.get("answer"))
        # Try to get the Exam or return CLOSED
        try:
            exam = Exam.objects.get(id = answer["exam"], active = True, closed = False)
            try:
                # Load and save the answers
                valid_alternatives = Alternative.objects.filter(question__exam = exam)
                new_aswer = Answer(name = answer['name'], exam = exam)
                new_aswer.save()
                for a in answer['answers']:
                    alternative = valid_alternatives.get(id = a)
                    Log(answer = new_aswer, question = alternative.question, alternative=alternative).save()
                # Check if any questions were not answered
                questions_answered = new_aswer.answers.all()
                questions_not_answered = exam.question_set.all().exclude(id__in=questions_answered)
                for q in questions_not_answered:
                    Log(answer = new_aswer, question = q, alternative=None).save()
                # Make Grade
                right = 0
                for l in Log.objects.filter(answer = new_aswer):
                    if l.alternative == l.question.right_alternative:
                        right += 1
                new_aswer.grade = (10.0/exam.question_set.all().count()) * right
                new_aswer.save()
            except Exception as e:
                print traceback.format_exc()
                response["message"] = "ERROR"
                pass
        except Exception as e:
            response["message"] = "EXAM_CLOSED"
            pass
        return make_response(response)

def serialize_exam(exam):
    new_exam = {
        "id": exam.id,
        "teacher": exam.user.first_name+" "+exam.user.last_name,
        "name": exam.name,
        "date": str(exam.date),
        "questions": []
    }
    for question in exam.question_set.all().order_by("?"):
        new_question = {
            "id": question.id,
            "text": question.text,
            "alternatives": []
        }
        for alternative in question.alternative_set.all().order_by("?"):
            new_alternative = {
                "id": alternative.id,
                "text": alternative.text
            }
            new_question["alternatives"].append(new_alternative)
        new_exam["questions"].append(new_question)
    return new_exam
