import re
from django.db import models
from users.models import UserModel


class QuizModel(models.Model):
    user = models.ManyToManyField(UserModel)
    title = models.CharField(max_length=128, blank=False)
    num_questions = models.IntegerField(default=5, blank=False)
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class QuestionModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=False)
    question_image = models.ImageField(upload_to="quiz_images" ,blank=True)
    final_ans = models.CharField(max_length=128)
    question_type = models.CharField(max_length=128)
    option1 = models.CharField(max_length=128, blank=True)
    option2 = models.CharField(max_length=128, blank=True)
    option3 = models.CharField(max_length=128, blank=True)
    option4 = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title


class ResultModel(models.Model):    
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"User:{self.user} Quiz: {self.quiz}"