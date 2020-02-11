from django.db import models

#from courses.models import Course
#Course.objects.all()
# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE,)

    #definiramo ponašanje razreda tu smo definirali redosljed pod razreda
    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title