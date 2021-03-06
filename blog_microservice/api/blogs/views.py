import requests
from django.contrib.auth.models import update_last_login
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializer, UserRegisterSerializer, UserLoginSerializer


class BlogViewset(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)
    def list(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, "data": serializer.data})
        print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = Blog.objects.get(id=pk)
        serializer = BlogSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Blog.objects.get(id=pk)
        serializer = BlogSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Blog.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = UserRegisterSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        print(user)
        data = {'username': serializer.validated_data['username'], 'password': serializer.validated_data['password']}
        print(data)
        token = requests.post("http://172.17.0.1:8000/api/token/", json=data)
        print(token.content.decode('utf8'))
        return JsonResponse({"token": token.content.decode('utf8')})
