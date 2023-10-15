

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'base'

router.register(r'kol', views.KOLViewSet, basename='kol')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'task', views.TaskViewSet, basename='task')
router.register(r'project', views.ProjectViewSet, basename='project')


urlpatterns = [
    path('', include(router.urls)),
]
