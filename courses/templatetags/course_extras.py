from django import template
from django.utils.safestring import mark_safe
import markdown2
from courses.models import Course

register = template.Library()
#ovo su tagovi
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

#ovo su filteri
@register.filter('time_estimate')
def time_estimate(word_count):
    '''estimates the number of minutes it  will take to complete a step
    based on the passed-in wordcount
    '''
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Coverts markdown text to html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
