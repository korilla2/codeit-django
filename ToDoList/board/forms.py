from django import forms
from .models import Board
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['subject', 'writer', 'content']
        widgets = {'subject': forms.TextInput(attrs={
            'class': 'subject',
            'placeholder': '제목을 입력 하세요'}),
            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요'}),
            'writer': forms.TextInput(attrs={'placeholder': '이름을 입력 하세요'})}
