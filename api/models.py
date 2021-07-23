from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Task(models.Model):
    """ Modelo de tarea """
    user = models.ForeignKey(User, on_delete=CASCADE)
    description = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.description
