from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Board
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request, 'board/index.html')


def create(request):
    data = Board(
        createdate=request.POST['createdate'], writer=request.POST['writer'], subject=request.POST['subject'], content=request.POST['content'])
    data.save()

    return render(request, 'board/detail.html', {'post': data})


def list(request):
    rows = Board.objects.all()
    content = {'rows': rows}
    return render(request, 'board/list.html', content)


def delete(request):
    post = Board.objects.get(id=request.GET['id'])
    post.delete()
    return HttpResponseRedirect(reverse('list'))


def detail(request, pk):
    post = Board.objects.get(id=pk)
    content = {'post': post}
    return render(request, 'board/detail.html', content)


def update(request):
    post = Board.objects.get(id=request.GET['id'])

    return render(request, 'board/update.html', {'post': post})


def modify(request):
    post = Board.objects.get(id=request.POST['id'])
    post.createdate = request.POST['createdate']
    post.subject = request.POST['subject']
    post.writer = request.POST['writer']
    post.content = request.POST['content']
    post.save()
    return HttpResponseRedirect(reverse('list'))
