from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Aqui se crean las tablas de la DB
#Luego con makemigrations y despues migrate
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        #Esto muestra el titulo de la tarea
        return self.title + ' by ' + self.user.username