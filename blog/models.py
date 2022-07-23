from django.db import models



# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo, self.author