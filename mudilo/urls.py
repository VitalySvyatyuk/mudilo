from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from app import views as v

urlpatterns = [
    url(r'^$', v.GrievanceView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^search$', v.SearchView.as_view(), name='search'),
    url(r'^success$', TemplateView.as_view(template_name='success.html'), name='success'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
]
