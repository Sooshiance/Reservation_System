from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    username   = models.CharField(max_length = 150)
    email      = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 150)
    last_name  = models.CharField(max_length = 150)

    def __str__(self):
        return f"{self.username} with USER_ID {self.user}"
