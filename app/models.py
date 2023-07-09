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