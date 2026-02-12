from django.db import models
from django.conf import settings
# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_code

class Material(models.Model):
    title = models.CharField(max_length=255)
    file_url = models.FileField(upload_to='materials/') 
    vote_count = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title