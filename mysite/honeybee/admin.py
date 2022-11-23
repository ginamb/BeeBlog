from django.contrib import admin
from .models import Post, Category, Comment, Honey, County


# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Honey)
admin.site.register(County)
