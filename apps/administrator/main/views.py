from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='proximo')
def home(request):
    return HttpResponseRedirect(reverse('index'))
