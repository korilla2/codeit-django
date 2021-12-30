from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Board(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    # writer = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdate = models.DateField(
        verbose_name='Date Created', auto_now_add=True)
    subject = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.subject


class Comment(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    # writer = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdate = models.DateField(
        verbose_name='Date Created', auto_now_add=True)
    subject = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.subject
