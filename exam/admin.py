from django.contrib import admin
from django.contrib import admin
from .models import Question, Exam

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'end']
    inlines = [QuestionInline,]


admin.site.register(Exam, ExamAdmin)
