from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=255)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task