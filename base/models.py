from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
