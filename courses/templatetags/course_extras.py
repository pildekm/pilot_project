from django import template
from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    ''' Dobijemo zadnji kreirani course object'''
    return Course.objects.latest('created_at')

# register.simple_tag('newest_course') ovo ili dekorator za registriranje taga

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''returns dict of courses to diplay nav pane'''
    courses = Course.objects.all()
    return {'courses': courses}

                       #(path do htmla)(ime funkcije)
# register.inclusion_tag('courses/course_nav.html')(nav_courses_list)
