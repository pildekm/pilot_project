from django.conf.urls import include, url
from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.course_list, name='Courses'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_detail, name='Step'),
    url(r'(?P<pk>\d+)$', views.course_detail, name='Detail'),

]
