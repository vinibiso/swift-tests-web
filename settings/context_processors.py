from django.contrib.sites.models import Site

def site_name(request):
    return { 'site': Site.objects.get_current() }
