from django.urls import path, include
# view와 연결
from . import views

urlpatterns = [
    # 해당 url 패턴을 views.py의 index 함수와 연결

    path('', views.index, name='index'),
    path('createTodo/', views.createTodo),
    path('list/', views.list),

]
