from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('modify/', views.modify, name='modify'),

]
