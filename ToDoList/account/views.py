from django.shortcuts import render
from .forms import LoginForm

# Create your views here.


def login(request):
    post_form = LoginForm()
    context = dict()
    context['form'] = post_form
    return render(request, 'account/login.html', context)
