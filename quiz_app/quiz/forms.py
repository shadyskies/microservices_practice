from .models import QuizModel, QuestionModel, AnswerModel
from django import forms


class AnswerForm(forms.ModelForm):
    # get options from model many to many field
    pass