from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    about = models.TextField(max_length=256, null=False)
    content = models.TextField(max_length=1024, null=False)
    author = models.CharField(max_length=100, null=False)
    image = models.FileField(null=True, upload_to='upload/')
    publish = models.DateTimeField(null=False, default=timezone.now())
    source = models.URLField(null=True)

    def __str__(self)-> str:
        return str(self.title)