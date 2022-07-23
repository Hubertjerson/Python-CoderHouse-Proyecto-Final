from django import forms

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    image = forms.ImageField(required=False)
    fecha_creacion = forms.DateTimeField(required=False)