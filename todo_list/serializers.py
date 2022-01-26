from rest_framework import serializers

from .models import Task, Image


class ImageListSerializer(serializers.ModelSerializer):
    """Вывод всех изображений"""

    class Meta:
        model = Image
        fields = '__all__'


class ImageDetailSerializer(serializers.ModelSerializer):
    """Вывод детального изображения"""
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    """Список задач"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True, many=False)
    for_who = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)

    class Meta:
        model = Task
        exclude = ('text', 'images')


class TaskDetailSerializer(serializers.ModelSerializer):
    """Полное описание задачи"""
    images = ImageListSerializer(read_only=True, many=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True, many=False)
    for_who = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('author', )