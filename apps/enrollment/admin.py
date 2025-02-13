from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import Enrollment, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name"]
    readonly_fields = ["password"]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["student", "course", "enrollment_date"]
    search_fields = ["student__name", "course__name"]
    list_filter = ["course"]
