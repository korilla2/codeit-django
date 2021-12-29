from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
    path('update2/', views.update2, name='update2'),
    path('create2/', views.create2, name='create2'),



]
