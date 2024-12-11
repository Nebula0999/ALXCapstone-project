from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
