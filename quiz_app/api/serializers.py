from rest_framework import serializers
from quiz.models import QuizModel, QuestionModel, AnswerModel


class QuizSerializer(serializers.ModelSerializer): 
    class Meta:
        model = QuizModel
        fields = ('title', 'deadline', 'num_questions')

        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('title', 'quiz', 'question_type', 'final_ans', 'question_image')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = ('title', 'question')