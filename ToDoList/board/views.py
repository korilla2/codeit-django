from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'board/index.html')


def login(request):
    return render(request, 'board/login.html')


def write(request):
    return render(request, 'board/write.html')
