from django.contrib import admin
from DjangoApp.models import BlogPost,Category


class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ['time']
    search_fields = ['title', 'body']
    list_display = ['title', 'category']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)