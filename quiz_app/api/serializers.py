from rest_framework import serializers
from quiz.models import QuizModel, QuestionModel


class QuizSerializer(serializers.ModelSerializer): 
    class Meta:
        model = QuizModel
        fields = ('title', 'deadline', 'num_questions')

        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('title', 'quiz', 'question_type', 'final_ans', 'question_image', 'option1', 'option2', 'option3', 'option4')
