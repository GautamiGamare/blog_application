from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *


# Create your views here.
class posts_list(APIView):
    def get(self, request, pk=None):
        if pk:
            data = Post.objects.get(id=pk)
            serializer = PostSerializer(data)
            return Response({'status':200, 'payload': serializer.data})
        else:
            data = Post.objects.all()
            paginator = PageNumberPagination()
            paginator.page_size = 1
            paginated_queryset = paginator.paginate_queryset(data, request)
            serializer = PostSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
    
class posts_update(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data = data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors, 'message':'Something went wrong!'})
        serializer.save()
        return Response({'status':200, 'message':'Data saved!'})

    def patch(self, request):
        try:
            data = Post.objects.get(id = request.data['id'])
            serializer = PostSerializer(data, request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status':403, 'error': serializer.errors, 'message': 'Something went wrong!'})
            serializer.save()
            return Response({'status':200, 'message':'Data saved!'})
        except Exception as e:
            return Response({'status': 400, 'message': 'Invalid id'})

    def delete(self, request):
        try:
            id = request.GET.get('id')
            data = Post.objects.get(id = id)
            data.delete()
            return Response({'status':200, 'message':'Data deleted!'})
        except Exception as e:
            return Response({'status': 400, 'message': 'Invalid id'})


class comments_list(APIView):
    def get(self, request):
        comment_obj = Comment.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 1
        paginated_queryset = paginator.paginate_queryset(comment_obj, request)
        serializer = CommentSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

class comments_create(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = CommentSerializer(data = data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors, 'message':'Something went wrong!'})
        serializer.save()
        return Response({'status':200, 'message':'Data saved!'})