from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title
