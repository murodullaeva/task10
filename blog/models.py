from django.contrib.auth.models import User
from django.db import models
class Friend(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    AUID = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.full_name