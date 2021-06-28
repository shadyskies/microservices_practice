from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer


class BlogViewset(viewsets.ViewSet):
    def list(self, request):
        products = Blog.objects.all()
        serializer = BlogSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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