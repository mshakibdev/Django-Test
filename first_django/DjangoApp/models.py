from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey('DjangoApp.Category', blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

