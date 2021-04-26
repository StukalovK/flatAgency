from django.db import models

class User(models.Model):
    nick_name = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=256, null=False)
    mob_phone = models.CharField(max_length=256, null=False)
    avatar = models.FileField(null=False, upload_to='upload/')
    address = models.TextField(max_length=1024, null=False)

