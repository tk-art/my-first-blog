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
    like_count = models.PositiveIntegerField(default=0)

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
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

    def __str__(self):
        return  f"Notification: {self.user} liked/commented on {self.item}"