from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    content = models.CharField(max_length=300, blank=False)
    title = models.CharField(max_length=128, blank=False)
    time_added = models.DateTimeField(auto_now_add=True)