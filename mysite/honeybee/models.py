from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name

    def get_absolute_url(self):
        return reverse('home')
        # return reverse('hello')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category =models.CharField(max_length=255, default='uncategorized')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Honey(models.Model):
    weight = models.IntegerField(max_length=255)
    honey = models.TextField(max_length=250)
    time = models.DateTimeField(max_length=250)
    # category =models.ForeignKey(Category, max_length=255, default='uncategorized')

    def __str__(self):
        return  str(self.weight) + str(self.honey) + str(self.time)

    # class Meta:
    #     verbose_name = 'Medus'
class County(models.Model):
    title = models.TextField(max_length=100)
