from django.db import models


# Create your models here.
class TodoItem(models.Model):
    text = models.TextField(default='', null=True)
