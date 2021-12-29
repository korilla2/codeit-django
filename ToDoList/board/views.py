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


def delete(request, pk):
    post = Board.objects.get(id=pk)
    post.delete()
    return HttpResponseRedirect(reverse('main'))


def detail(request, pk):
    post = Board.objects.get(id=pk)
    content = {'post': post}
    return render(request, 'board/detail.html', content)


def update(request, pk):
    post = Board.objects.get(id=pk)
    post.save()

    return render(request, 'board/update2.html', {'post': post})


def update2(request):
    data = Board(
        createdate=request.POST['createdate'], writer=request.POST['writer'], subject=request.POST['subject'], content=request.POST['content'])

    data.save()

    return render(request, 'board/detail.html', {'data': data})


def create2(request):
    data = Board(
        createdate=request.POST['createdate'], writer=request.POST['writer'], subject=request.POST['subject'], content=request.POST['content'])
    data.save()

    return render(request, 'board/detail.html', {'post': data})
