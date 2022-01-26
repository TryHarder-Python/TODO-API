from django.core.mail import send_mail
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

    def create(self, validated_data):
        # Когда создается таска отправляется эмеил в консоль
        task_obj = super().create(validated_data)
        send_mail(
            f'{task_obj.title} for you',
            'This Task for you',
            'exampleemail@gmail.com',
            [user.email for user in task_obj.for_who.all()]
        )
        print([i.email for i in task_obj.for_who.all()])
        return task_obj
