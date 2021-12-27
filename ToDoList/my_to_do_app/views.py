from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
    # user_input_str = request.POST['todoContent']
    # return HttpResponse(f'사용자가 입력한 값: {user_input_str}')

    user_input_str = request.POST['todoContent']
    # models.py에서 정의된 클래스를 이용해 전달받은 값을 DB에 저장
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


def list(request):
    return render(request, 'my_to_do_app/list.html')
