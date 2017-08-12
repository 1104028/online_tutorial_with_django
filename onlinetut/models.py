from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Courses(models.Model):
    course_title = models.CharField(max_length=500)
    Teacher_name = models.CharField(max_length=500)
    course_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('courselist', kwargs={'pk': self.pk})

    def __str__(self):
        return self.course_title + '-' + self.Teacher_name


class Tutorials(models.Model):
    albums = models.ForeignKey(Courses,on_delete=models.CASCADE)
    lecture_title = models.CharField(max_length=250)
    lecture_video = models.FileField()

    def __str__(self):
        return self.lecture_title