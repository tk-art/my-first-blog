from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # fields
    groups = None
    user_permissions = None
