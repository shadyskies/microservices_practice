from .models import QuizModel, QuestionModel
from django import forms


class QuizForm(forms.ModelForm):
    # get options from model many to many field
    class Meta:
        model = QuizModel
        fields = "__all__"

