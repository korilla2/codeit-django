from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('login/', views.login, name='login'),
    path('write/', views.write, name='write'),
]
