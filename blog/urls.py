from django.urls import path
from .views import blog_post, home,blog_get,about

urlpatterns = [
    path('', home,name='home'),
    path('blog/', blog_post,name='blog_post'),
    path('crearblog/', blog_get,name='blog_get'),
    path('about/', about,name='about'),
]
