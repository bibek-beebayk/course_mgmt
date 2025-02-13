from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from apps.course.models import Course

User = get_user_model()


class Student(models.Model):
    name = models.CharField(max_length=256)    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    enrollment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
