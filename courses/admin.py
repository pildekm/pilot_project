from django.contrib import admin
from . import models

# class TextInline(admin.StackedInline):
#     model = models.Text

# class CourseAdmin(admin.ModelAdmin):
#     inlines = [TextInline, ]


# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Text)
admin.site.register(models.Quiz)
# admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.MultipleChoiceQuestion)
admin.site.register(models.TrueFalseQuestion)

