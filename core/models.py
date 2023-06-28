from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmailNotification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='email_notification')
    email = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
