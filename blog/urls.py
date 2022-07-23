from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('blog/', views.lista_post,name='blog_post'),
    path('crearblog/', views.formulario_blog,name='blog_get'),
    path('editar-blog/<int:id>/', views.editar_blog,name='editar_blog'),
    path('eliminar-blog/<int:id>/', views.eliminar_blog,name='eliminar_blog'),
    path('about/', views.about,name='about'),
]
