from django.contrib import admin
from .models import QuizModel, QuestionModel, ResultModel


admin.site.register(QuizModel)
admin.site.register(QuestionModel)
admin.site.register(ResultModel)