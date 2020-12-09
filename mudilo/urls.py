from django.conf.urls import url
from django.contrib import admin

from app import views as v

urlpatterns = [
    url(r'^$', v.GrievanceView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^search$', v.SearchView.as_view(), name='search'),
]
