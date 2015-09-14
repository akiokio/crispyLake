from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    paginate_by = 100

    def get_queryset(self):
        todos = Todo.objects.filter(owner=self.request.user.id)
        return todos

