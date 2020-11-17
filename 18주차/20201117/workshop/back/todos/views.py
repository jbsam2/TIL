from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def todo_list_create(request):
    #todo database에서 todo 정보를 모두 긁어서 JSON응답
    # model => QuerySet => dict, string => JSON응답
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(request.user.todos, many=True)
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def todo_delete_update(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)

    if not request.user.todos.filter(pk=todo_pk).exists(): #작성자가 아닌 다른 사람이 수정하고자 하면 경고문을 보내준다.
        return Response({'detail':'권한이 없습니다.'})
        
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
    else:
        todo.delete()
        return Response({ 'id': todo_pk })