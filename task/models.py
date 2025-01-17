from django.db import models
import datetime

class Task(models.Model):
    task_title = models.CharField(max_length=255) 
    task_description = models.TextField()  
    is_completed = models.BooleanField(default=False)  
    assign_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.task_title
