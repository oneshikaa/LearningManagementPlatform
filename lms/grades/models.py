from django.db import models
from django.db import models
from django.contrib.auth.models import User
from curriculum.models import Subject
from django.template.defaultfilters import slugify

# Create your models here.
class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Subject, on_delete=models.CASCADE)  
    grade = models.CharField(max_length=2)  
    
    def __str__(self):
        return f"{self.student.username} - {self.course.name}: {self.grade}"



