from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^provas/', include('apps.administrator.exams.urls')),
    # Login, Logout, Password Reset and Change
    url(r'^$', auth_views.login, {'template_name': 'login.html', 'extra_context': {'next': '/provas/'}}, name = 'login'),
    url(r'^logout/', auth_views.logout_then_login, name = 'logout'),
    url(r'^trocarsenha/sucesso/', auth_views.password_change_done, {'template_name': 'reset/password_change_done.html'}, name = 'change-done'),
    url(r'^trocarsenha/', auth_views.password_change, {'template_name': 'reset/password_change.html', 'post_change_redirect': '/trocarsenha/sucesso/'}, name = 'change'),
    url(r'^esqueciminhasenha/', auth_views.password_reset, {
            'template_name': 'reset/password_reset.html',
            'email_template_name': 'reset/nohtmlemail.html',
            'subject_template_name': 'reset/subject.txt',
            'post_reset_redirect': '/emailenviado/',
            'from_email': 'Layer | Site <layerdd@gmail.com>',
            'html_email_template_name': 'reset/email.html'
        }, name = 'reset'),
    url(r'^emailenviado/', auth_views.password_reset_done, {'template_name': 'reset/password_reset_done.html', }, name = 'reset-email-sent'),
    url(r'^confirmarsenha/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.password_reset_confirm, {'template_name': 'reset/password_reset_confirm.html', 'post_reset_redirect': '/feito/'}, name = 'reset-confirm'),
    url(r'^feito/', auth_views.password_reset_done, {'template_name': 'reset/password_reset_completed.html', }, name = 'reset-completed'),
]
