from django.urls import path
from . import views

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'tasks', views.TaskViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = router.urls