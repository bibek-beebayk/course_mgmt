import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from apps.course.models import Course

User = get_user_model()


class Student(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=1000, blank=True, null=True)

    def generate_random_password(self, length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        result_str = "".join(random.choice(characters) for i in range(length))
        return result_str

    def save(self, *args, **kwargs):
        created = self.pk is None
        if created:
            password_str = self.generate_random_password()
            self.password = make_password(password_str)
        else:
            original_password = Student.objects.get(pk=self.pk).password
            if original_password != self.password:
                self.password = make_password(self.password)
        super().save(*args, **kwargs)

        if created:
            send_mail(
                "Account Created",
                f"Your account has been successfully created. Use password {password_str} to login.",
                settings.FROM_EMAIL,
                [self.email],
                fail_silently=False,
            )

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
        return f"{self.student.name} enrolled in {self.course.title}"

    class Meta:
        unique_together = [["student", "course"]]
