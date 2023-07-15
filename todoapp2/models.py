from django.db import models
from django.contrib.auth.models import User
class TodoTask(models.Model):
    task = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.task


