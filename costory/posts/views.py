from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = dict()
    context['posts'] = posts
    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = dict()
    context['post'] = post
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        new_post = post_form.save()
        return redirect('post-detail', post_id=new_post.id)
    else:
        post_form = PostForm()
        context = dict()
        context['form'] = post_form
        return render(request, 'posts/post_form.html', context)
