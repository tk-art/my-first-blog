from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # fields
    groups = None
    user_permissions = None

class Item(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    deadline = models.DateField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='item_images/')
    place = models.CharField(max_length=100)
    like_count = models.PositiveIntegerField(default=0)

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models. CASCADE)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_images/')
    content = models.TextField()

class Message(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
