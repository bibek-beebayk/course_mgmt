from django.contrib import admin
from .models import Student, Enrollment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name"]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["student", "course", "enrollment_date"]
    search_fields = ["student__name", "course__name"]
    list_filter = ["course"]