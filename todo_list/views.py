from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task, Image
from .permissions import IsAuthorOrIsAuthenticated

from .serializers import (
    TaskListSerializer,
    TaskDetailSerializer,
    ImageListSerializer,
    ImageDetailSerializer,
    TaskUpdateCreateSerializer)

not_list_actions = ('retrieve', 'update', 'partial_update', 'create', 'destroy')


class TaskViewSet(viewsets.ModelViewSet):
    """View для всех опираций над задачами"""
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrIsAuthenticated]
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        elif self.action == 'retrieve':
            return TaskDetailSerializer
        elif self.action in ('update', 'partial_update', 'create', 'destroy'):
            return TaskUpdateCreateSerializer

    def perform_create(self, serializer):
        """Тот кто создал тот и автор"""
        serializer.save(author=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    """Вывод ссылок на изображения и загрузка изображений"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Image.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ImageListSerializer
        elif self.action in not_list_actions:
            return ImageDetailSerializer





