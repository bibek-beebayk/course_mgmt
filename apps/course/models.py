from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validate_video(value):
    max_size = 50*1024*1024
    if value.size > max_size:
        raise ValidationError("Max file size allowed is 50 mb")


def validate_document(value):
    max_size = 10*1024*1024
    if value.size > max_size:
        raise ValidationError("Max file size allowed is 10 mb")

class Category(models.Model):
    name = models.CharField(max_length=100)
    priority = models.PositiveIntegerField()
    parent = models.ForeignKey("self", on_delete=models.PROTECT, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="courses")


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/", validators=[FileExtensionValidator(["mp4"]), validate_video])

    def __str__(self):
        return self.title
    

class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="documents")
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to="documents/", validators=[FileExtensionValidator(["pdf"]), validate_document])

    def __str__(self):
        return self.title
    

class MCQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="mcqs")
    question_text = models.TextField()

    def __str__(self):
        return self.question_text
    

class MCQOption(models.Model):
    mcq = models.ForeignKey(MCQ, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text
