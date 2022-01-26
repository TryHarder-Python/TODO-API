from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task, Image
from .permissions import IsAuthorOrIsAuthenticated

from .serializers import TaskListSerializer, TaskDetailSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """View для всех опираций над задачами"""
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrIsAuthenticated]
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        elif self.action in ('retrieve', 'update', 'partial_update', 'create', 'destroy'):
            return TaskDetailSerializer

    def perform_create(self, serializer):
        """Тот кто создал тот и автор"""
        serializer.save(author=self.request.user)





