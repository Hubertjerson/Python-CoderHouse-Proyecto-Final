from django import forms
from ckeditor.fields import RichTextFormField

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    description = RichTextFormField()
    image = forms.ImageField(required=False)
    fecha_creacion = forms.DateTimeField(required=False)
    
class BusquedaAuthor(forms.Form):
    author = forms.CharField(max_length=30, required=False)