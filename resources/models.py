from django.db import models
from django.conf import settings
# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

class Material(models.Model):
    title = models.CharField(max_length=255)
    file_url = models.FileField(upload_to='materials/') 
    vote_count = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='materials',
        null=True, 
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title