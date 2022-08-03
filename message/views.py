from django.dispatch import receiver
from django.shortcuts import render
from message.models import *
from message.forms import *

# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

# Django authentication

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MensajeLista(LoginRequiredMixin, ListView):

    model = Message
    template_name = "message/message_list.html"

class MensajeDetalle(LoginRequiredMixin, DetailView):

    model = Message
    template_name = "message/message_detail.html"

class CrearMensaje(LoginRequiredMixin, CreateView):

    model = Message
    success_url = "/messages/"
    fields = ['titulo','sender', 'reciever', 'contenido', 'fecha']


class EliminarMensaje(LoginRequiredMixin, DeleteView):

    model = Message
    success_url = "/messages/"