from django.contrib import admin
from .models import QuizModel, QuestionModel, AnswerModel, ResultModel


admin.site.register(QuizModel)
admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
admin.site.register(ResultModel)