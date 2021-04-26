from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    #
    name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return str(self.name)


class District(models.Model):
    #
    name = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return str(self.name)


class Offer(models.Model):
    #
    title = models.CharField(max_length=100, null=False)
    about = models.TextField(max_length=256, null=False)
    content = models.TextField(max_length=1024, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, null=False)
    floor = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    publish = models.DateTimeField(null=False, default=timezone.now())
    single_image = models.FileField(null=True, upload_to='demo/')

    def __str__(self) -> str:
        return str(self.title)


class Picture(models.Model):
    #
    path = models.FileField(null=False, upload_to='flats/')
    legend = models.CharField(max_length=256, null=False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.legend)

