from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from board import views as board_views

urlpatterns = [
    path('', views.index, name='main'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('modify/', views.modify, name='modify'),
    path('login_temp/', views.login_temp, name='login_temp'),
    path('login/',
         auth_views.LoginView.as_view(template_name='board/login.html'), name='login'),
    path('correct_login/', views.correct_login, name='correct'),
    path('signup/', views.signup, name='signup'),
    path('createUser/', views.createUser, name='createUser'),
    path('accounts/profile/', board_views.index),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('comment/', views.comment, name='comment'),
    path('comment2/', views.comment, name='comment'),
    path('detail2/<int:pk>', views.detail2, name='detail2'),




]
