# coding: utf-8
from django .template import Library
from blog.models import Post, Category, Tag
from django.db.models.aggregates import Count

register = Library()

@register.simple_tag
def get_last_post(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def get_date():
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_category():
    return Category.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)
