#ctbot_backend/core/models.py
from django.db import models
from django.contrib.auth.models import User

class API(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"API for {self.user.username}"

