import re
from django.shortcuts import render
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required


class QuizView(APIView):
    def post(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer is valid")
            obj = serializer.save()
            return Response(data={"status": status.HTTP_201_CREATED,  "quiz_id":obj.id})
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

class QuestionView(APIView):
    def post(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer is valid")
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
            