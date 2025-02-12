from django.contrib import admin
from .models import Course, MCQOption, Video, Document, Category, MCQ
from nested_admin import NestedTabularInline, NestedModelAdmin

class VideoInline(NestedTabularInline):
    model = Video
    extra = 0


class DocumentInline(NestedTabularInline):
    model = Document
    extra = 0

class MCQOptionInline(NestedTabularInline):
    model = MCQOption
    extra = 0

class MCQInline(NestedTabularInline):
    model = MCQ
    extra = 0
    inlines = [MCQOptionInline]


# @admin.register(MCQ)
# class MCQAdmin(NestedModelAdmin):
#     list_display = ["question_text", "course"]
#     search_fields = ["question_text"]
#     list_filter = ["course"]
#     inlines = [MCQOptionInline]

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(course__in=request.user.courses.all())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "parent" ]
    search_fields = ["name"]

@admin.register(Course)
class CourseAdmin(NestedModelAdmin):
    list_display = ["title", "category", "price"]
    list_filter = ["category"]
    search_fields = ["title"]
    inlines = [VideoInline, DocumentInline, MCQInline]
