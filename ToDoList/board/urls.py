from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
