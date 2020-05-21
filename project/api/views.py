from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from blog.models import Post
from api.serializers import PostSerializer
# from api.serializers import RegistrationSerializer


# blog views
@api_view(['GET'])
def api_detail_blog_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(['PUT'])
def api_update_blog_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete_blog_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = post.delete()
        data = {}
        if operation:
            data['sucess'] = 'delete successful'
        else:
            data['failure'] = 'detele failed'
        return Response(data=data)


@api_view(['POST'])
def api_create_blog_view(request):
    account = User.objects.get(pk=1)
    post = Post(author=account)

    if request.method == 'POST':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User views
# @api_view(['POST'])
# def api_registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             user = serializer.save()
#             data['response'] = 'successfully registered a new user'
#             data['email'] = user.email
#             data['username'] = user.username
#         else:
#             data = serializer.errors
#         return Response(data)