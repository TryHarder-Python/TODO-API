from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task, Image


class TaskListSerializer(serializers.ModelSerializer):
    """Список задач"""
    class Meta:
        model = Task
        exclude = ('text', 'images')


class TaskDetailSerializer(serializers.ModelSerializer):
    """Полное описание задачи"""
    class Meta:
        model = Task
        exclude = ('author', )
