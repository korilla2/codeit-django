from .models import Post


def validate_post():

    posts = Post.objects.all()

    for post in posts:
        if '&' in post.content:
            print(post.id, '&')
            post.content = post.content.replace('&', '')
            post.save()
        if post.dt_modified < post.dt_created:
            print(post.id, '날짜')
            post.save()
