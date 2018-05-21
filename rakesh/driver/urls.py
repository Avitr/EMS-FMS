from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from driver import views
 
urlpatterns = [
    url(r'^driver/$', views.DriverList.as_view()),
    url(r'^driver/(?P<pk>[0-9]+)/$', views.DriverDetail.as_view()),
]