from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from .sitemaps import StaticViewSitemap
from app import views as v
from app import api as api_v

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', v.GrievanceView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^search$', v.SearchView.as_view(), name='search'),
    url(r'^success$', TemplateView.as_view(template_name='success.html'), name='success'),
    url(r'^error$', TemplateView.as_view(template_name='error.html'), name='error'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),

    url(r'^api/v1/search$', api_v.SearchPlates.as_view(), name='api_search'),

    # path('api-auth/', include('rest_framework.urls'))

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
