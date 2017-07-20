from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author',  'create_time', 'last_time']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
