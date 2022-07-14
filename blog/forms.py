from distutils.command.upload import upload
from django import forms

class FormBlog(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    image = forms.ImageField(required=False)
    fecha_creacion = forms.DateTimeField(required=False)