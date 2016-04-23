from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
admin.autodiscover()

urlpatterns = [
    url(r'', include("apps.administrator.main.urls")),
    url(r'^api/', include("apps.api.urls")),
    # url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': { 'static': StaticViewSitemap }}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^admin/', include(admin.site.urls)),
]
