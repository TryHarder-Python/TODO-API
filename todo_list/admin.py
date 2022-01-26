from django.contrib import admin
from .models import Task, Image


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass