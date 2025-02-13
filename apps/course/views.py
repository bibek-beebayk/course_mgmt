from django.shortcuts import redirect, render

from apps.course.models import Course
from apps.enrollment.models import Enrollment, Student


def index(request):
    if request.method == "POST":
        selected = [int(x) for x in request.POST.getlist("students")]
        course_id = request.POST.get("course")
        course = Course.objects.get(id=course_id)

        existing = course.enrollments.values_list("student", flat=True)
        to_delete = list(set(existing) - set(selected))

        Enrollment.objects.filter(student__id__in=to_delete, course=course).delete()

        for id in selected:
            Enrollment.objects.get_or_create(student_id=id, course=course)
        return redirect("index")

    context = {}
    context["courses"] = Course.objects.all()
    context["students"] = Student.objects.all()
    return render(request, "index.html", context)
