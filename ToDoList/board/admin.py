from django.contrib import admin

from .models import Board

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('createdate', 'user', 'subject')

    list_display_links = ['subject']


admin.site.register(Board, BoardAdmin)
