# Django
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Project

class NoCSRFMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(NoCSRFMixin, self).dispatch(*args, **kwargs)
