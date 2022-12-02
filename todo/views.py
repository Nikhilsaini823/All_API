from rest_framework import generics

from todo import models
from todo.models import Todo
from .serializer import TodoSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from snippets.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class ListTodo(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(owner_id=self.request.user.id)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(owner_id=self.request.user.id)

class TodoUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly, IsAuthenticated]


    def put(self, request, pk):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Todo, pk=pk)
        # this is the only field we want to update
        data = {"task_status": 'COMPLETE'}
        serializer = TodoSerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=get_object_or_404)

    def delete(self, request, pk, format=None):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response({'message': 'Record deleted successfully' })
