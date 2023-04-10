from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer



@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        objs = Post.objects.all()
        print(objs)
        serializer = PostSerializer(objs, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
