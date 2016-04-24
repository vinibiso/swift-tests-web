from django.conf.urls import url
from . import views

urlpatterns = [
    # Alternative
    url(r'^prova/(?P<exam>[0-9]+)/question/(?P<question>[0-9]+)/alternative/add/$', views.AlternativeCreate.as_view(), name = 'alternative_add'),
    url(r'^prova/(?P<exam>[0-9]+)/question/(?P<question>[0-9]+)/alternative/(?P<pk>[0-9]+)/update/$', views.AlternativeUpdate.as_view(), name = 'alternative_update'),
    url(r'^prova/(?P<exam>[0-9]+)/question/(?P<question>[0-9]+)/alternative/(?P<pk>[0-9]+)/delete/$', views.AlternativeDelete.as_view(), name = 'alternative_delete'),
    # Questions
    url(r'^prova/(?P<exam>[0-9]+)/questao/add/$', views.QuestionCreate.as_view(), name = 'question_add'),
    url(r'^prova/(?P<exam>[0-9]+)/questao/(?P<pk>[0-9]+)/update/$', views.QuestionUpdate.as_view(), name = 'question_update'),
    url(r'^prova/(?P<exam>[0-9]+)/questao/(?P<pk>[0-9]+)/delete/$', views.QuestionDelete.as_view(), name = 'question_delete'),
    url(r'^prova/(?P<exam>[0-9]+)/questao/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name = 'question_detail'),
    # Exams
    url(r'^prova/(?P<exam>[0-9]+)/relatorio/data/$', views.ExamReportData.as_view(), name = 'exam_report_data'),
    url(r'^prova/(?P<exam>[0-9]+)/relatorio/$', views.ExamReport.as_view(), name = 'exam_report'),
    url(r'^prova/(?P<exam>[0-9]+)/delete/$', views.ExamDelete.as_view(), name = 'exam_delete'),
    url(r'^prova/(?P<exam>[0-9]+)/close/$', views.ExamCloseView.as_view(), name = 'exam_close'),
    url(r'^prova/(?P<exam>[0-9]+)/activate/$', views.ExamActivateView.as_view(), name = 'exam_activate'),
    url(r'^prova/add/$', views.ExamCreate.as_view(), name = 'exam_add'),
    url(r'^prova/(?P<exam>[0-9]+)/update/$', views.ExamUpdate.as_view(), name = 'exam_update'),
    url(r'^prova/(?P<exam>[0-9]+)/$', views.ExamDetail.as_view(), name = 'exam_detail'),
    url(r'^(?P<page>[0-9]+)/$', views.ExamList.as_view(), name = 'exam_list_pag'),
    url(r'^$', views.ExamList.as_view(), name = 'exam_list'),
]
