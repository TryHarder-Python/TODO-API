from django.urls import path
from . import views

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'tasks', views.TaskViewSet)

urlpatterns = router.urls