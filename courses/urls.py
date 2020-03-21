from django.conf.urls import include, url
from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.course_list, name='Courses'),
url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)$', views.text_detail, name='Text'),
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)$', views.quiz_detail, name='Quiz'),
    url(r'(?P<pk>\d+)$', views.course_detail, name='Detail'),

]
