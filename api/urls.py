# api/urls.py

from django.urls import path

from .views import ArticleViewSet

urlpatterns = [
    path('articles/', ArticleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('articles/<int:pk>/', ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]