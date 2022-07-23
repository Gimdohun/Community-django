from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_main, name='community_main'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('register/', views.register, name='register'),
]