from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text
