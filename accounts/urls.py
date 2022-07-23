from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login , name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html') , name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar, name='editar'),
]
