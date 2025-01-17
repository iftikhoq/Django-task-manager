from django.db import models
from task.models import Task

class Category(models.Model):
    category_name = models.CharField(max_length=255) 
    tasks = models.ManyToManyField(Task, related_name='categories')  

    def __str__(self):
        return self.category_name