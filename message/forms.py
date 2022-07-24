from django import forms

class MessagesForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    sender = forms.CharField(max_length=60)
    reciever = forms.CharField(max_length=60)
    contenido = forms.CharField(max_length=1000)
    fecha = forms.DateField()