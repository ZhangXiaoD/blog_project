import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=150, blank=True)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)
    page_view = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def add_page_view(self):
        self.page_view += 1
        self.save(update_fields=['page_view'])

    def save(self, *args, **kwargs):
        if not self.summary:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite'])
            self.summary = strip_tags(md.convert(self.body))[:54]
        super(Post,self).save(*args, **kwargs)

    class Meta:
        ordering = ['-create_time']