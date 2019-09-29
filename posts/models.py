from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


def upload_image_to(instance, filename):
    return 'post/post_{0}/{1}'.format(instance.title, filename)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to=upload_image_to)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]
