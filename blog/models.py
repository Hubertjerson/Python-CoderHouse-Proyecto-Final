from contextlib import nullcontext
from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)