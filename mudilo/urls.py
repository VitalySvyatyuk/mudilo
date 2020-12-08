from django.conf.urls import url
from django.contrib import admin

from app import views as v

urlpatterns = [
    url(r'^$', v.GrievanceView.as_view(), name='home'),  # grievance_create, plate_get
    url(r'^admin/', admin.site.urls),

]
