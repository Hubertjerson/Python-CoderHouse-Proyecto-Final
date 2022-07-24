from django.urls import path
from message.views import *

urlpatterns = [
    path('', mensaje_lista.as_view(), name="Messages"),
    path('new/', crear_mensaje.as_view(), name="New_message"),
    path('<pk>/', mensaje_detalle.as_view(), name="Message_detail"),
    path('delete/<pk>', eliminar_mensaje.as_view(), name="Delete_message"),
]
