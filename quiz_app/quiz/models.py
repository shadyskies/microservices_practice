from django.db import models
from users.models import UserModel


class QuizModel(models.Model):
    user = models.ManyToManyField(UserModel)
    title = models.CharField(max_length=128, blank=False)
    data_submitted = models.DateTimeField(blank=True, null=True)
    num_questions = models.IntegerField(default=5, blank=False)
    deadline = models.DateTimeField(blank=True, null=True)

class QuestionModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=False)
    question_image = models.ImageField(null=True, blank=True)
    final_ans = models.CharField(max_length=128)
    question_type = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title