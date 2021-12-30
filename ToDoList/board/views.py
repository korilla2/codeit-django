from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Board, Comment

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'board/index.html')


def comment(request):

    return render(request, 'board/comment.html')


def comment2(request):

    data = Comment(
        createdate=request.POST['createdate'], user=request.user, subject=request.POST['subject'], content=request.POST['content'])
    print(data)
    data.save()
    return render(request, 'board/detail2.html', {'post': data})


@login_required(login_url='/board/login/')
def create(request):
    if request.method == "POST":
        data = Comment(
            createdate=request.POST['createdate'], user=request.user, subject=request.POST['subject'], content=request.POST['content'])
        data.save()
        return render(request, 'board/detail.html', {'post': data})

    else:
        return render(request, 'board/index.html')


def list(request):
    rows = Board.objects.all()
    posts = Comment.objects.all()
    content2 = {'posts': posts}
    content = {'rows': rows}
    return render(request, 'board/list.html', content)


@login_required(login_url='/board/login/')
def delete(request):
    post = Board.objects.get(id=request.GET['id'])
    if request.user.is_authenticated:
        if request.user.username == post.user.username:
            post.delete()
            return HttpResponseRedirect(reverse('list'))
        else:
            return HttpResponseRedirect(reverse('list'))
    else:
        return render(request, 'board/index.html')


def detail(request, pk):
    post = Board.objects.get(id=pk)
    content = {'post': post}
    return render(request, 'board/detail.html', content)


def detail2(request, pk):
    post = Comment.objects.get(id=pk)
    content = {'post': post}
    return render(request, 'board/detail.html', content)


@login_required(login_url='/board/login/')
def update(request):
    post = Board.objects.get(id=request.GET['id'])

    if request.user.is_authenticated:
        if request.user.username == post.user.username:
            return render(request, 'board/update.html', {'post': post})
        else:
            return HttpResponseRedirect(reverse('list'))
    else:
        return render(request, 'board/index.html')


@login_required(login_url='/board/login/')
def modify(request):
    post = Board.objects.get(id=request.POST['id'])
    post.createdate = request.POST['createdate']
    post.subject = request.POST['subject']
    post.writer = request.POST['writer']
    post.content = request.POST['content']
    post.save()
    return HttpResponseRedirect(reverse('list'))


def login_temp(request):
    return render(request, 'board/login.html')


def correct_login(request):
    return render(request, 'board/correct_login.html')


def signup(request):
    return render(request, 'board/signup.html')


def createUser(request):
    user = User(username=request.POST['id'],
                password=make_password(request.POST['pw']))
    user.save()
    return HttpResponseRedirect(reverse('main'))
