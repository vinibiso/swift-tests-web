from django.conf.urls import url
from . import views

urlpatterns = [
    # Alternative
    url(r'^prova/(?P<exam>[0-9]+)/question/(?P<question>[0-9]+)/alternative/add/$', views.AlternativeCreate.as_view(), name = 'alternative_add'),
    url(r'^prova/(?P<exam>[0-9]+)/question/(?P<question>[0-9]+)/alternative/(?P<pk>[0-9]+)/update/$', views.AlternativeUpdate.as_view(), name = 'alternative_update'),
    # Questions
    url(r'^prova/(?P<exam>[0-9]+)/questao/add/$', views.QuestionCreate.as_view(), name = 'question_add'),
    url(r'^prova/(?P<exam>[0-9]+)/questao/(?P<pk>[0-9]+)/update/$', views.QuestionUpdate.as_view(), name = 'question_update'),
    url(r'^prova/(?P<exam>[0-9]+)/questao/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name = 'question_detail'),
    # Exams
    url(r'^prova/add/$', views.ExamCreate.as_view(), name = 'exam_add'),
    url(r'^prova/(?P<exam>[0-9]+)/update/$', views.ExamUpdate.as_view(), name = 'exam_update'),
    url(r'^prova/(?P<exam>[0-9]+)/$', views.ExamDetail.as_view(), name = 'exam_detail'),
    url(r'^(?P<page>[0-9]+)/$', views.ExamList.as_view(), name = 'exam_list_pag'),
    url(r'^$', views.ExamList.as_view(), name = 'exam_list'),
]
