from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='tests.html') , name = 'api_tests'),
    url(r'^send_exam/$', views.SendExamView.as_view(), name = 'api_send'),
    url(r'^receive_vote/$', views.ReceiveVoteView.as_view(), name = 'api_receive'),
]
