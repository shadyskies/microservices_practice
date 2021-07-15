from django.db import models
from django.contrib.auth.models import User



class QuizModel(models.Model):
    user = models.ManyToManyField(User)
    data_submitted = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(auto_now_add=True)

class QuestionModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=False)
    question_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text