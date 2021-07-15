from quiz.models import QuizModel, QuestionModel, AnswerModel
from django import forms


class CreateQuizForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget())
    class Meta:
        model = QuizModel
        fields = ['title', 'deadline', 'user', 'num_questions']


choices = (
    ('mcq', 'mcq'),
    ('text', 'text'),
)

class CreateQuestionForm(forms.ModelForm):
    question_type = forms.ChoiceField(choices=choices) 
    class Meta:
        model = QuestionModel
        fields = ['title', 'question_type', 'question_image', 'final_ans' ,'quiz']


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = ['question' , 'title']