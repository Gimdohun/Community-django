from django.urls import path
from . import views

app_name = 'userdb'

urlpatterns = [
    path('register/', views.register, name='register'),
]