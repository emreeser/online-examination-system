from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Exam(models.Model):
    title = models.CharField(max_length=200, default='')
    start = models.DateTimeField(verbose_name='Exam starting time')
    end = models.DateTimeField(verbose_name='Exam ending time')

    def is_active(self):
        now = timezone.now()
        if self.start <= now and self.end > now:
            return True
        return False

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=False)
    question = models.TextField(null=False, blank=False)
    optionA = models.CharField(verbose_name='Option A', max_length=200, null=False, blank=False)
    optionB = models.CharField(verbose_name='Option B', max_length=200, null=False, blank=False)
    optionC = models.CharField(verbose_name='Option C', max_length=200, null=False, blank=False)
    optionD = models.CharField(verbose_name='Option D', max_length=200, null=False, blank=False)

    def __str__(self):
        return self.question[:10]

class QuestionSet(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
