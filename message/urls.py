from django.urls import path
from message.views import *

urlpatterns = [
    path('', MensajeLista.as_view(), name="Messages"),
    path('new/', CrearMensaje.as_view(), name="New_message"),
    path('<pk>/', MensajeDetalle.as_view(), name="Message_detail"),
    path('delete/<pk>', EliminarMensaje.as_view(), name="Delete_message"),
]
