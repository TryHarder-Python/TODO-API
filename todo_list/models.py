from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    """Todo задача"""
    title = models.CharField('Заголовок', max_length=150)
    text = models.TextField('Текст')
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', on_delete=models.CASCADE, related_name='author')
    for_who = models.ManyToManyField(
        get_user_model(),
        verbose_name='Для кого',
        related_name='for_who',
        blank=True)
    create_at = models.DateTimeField('Создано', auto_now_add=True)
    update_at = models.DateTimeField('Обновленно', auto_now=True)
    images = models.ManyToManyField('Image',
                                    verbose_name='Изображения',
                                    related_name='task_image',
                                    blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'


class Image(models.Model):
    """Изображения"""
    image = models.ImageField(upload_to='task_image/')
    create_at = models.DateTimeField('Загруженно', auto_now_add=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'


