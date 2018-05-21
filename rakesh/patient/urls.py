from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from patient import views
 
urlpatterns = [
    url(r'^patient/$', views.PatientList.as_view()),
    url(r'^patient/(?P<pk>[0-9]+)/$', views.PatientDetail.as_view()),
]