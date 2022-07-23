from datetime import datetime
from django.shortcuts import redirect, render

from blog.forms import FormBlog
from blog.models import Blog
# Create your views here.


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def lista_post(request):
    posts = Blog.objects.all()
    return render(request, 'blogPost.html', {'posts': posts})


def formulario_blog(request):

    if request.method == 'POST':
        form = FormBlog(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now()

            post_public = Blog(
                titulo=data.get('titulo'),
                subtitulo=data.get('subtitulo'),
                author=data.get('author'),
                description=data.get('description'),
                image=data.get('image'),
                fecha_creacion=fecha,
            )
            post_public.save()

            return redirect('blog_post')
        else:
            return render(request, 'blogGet.html', {'posts': form})
    form_blog = FormBlog()

    return render(request, 'blogGet.html', {'form': form_blog})


def editar_blog(request, id):
    post = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = FormBlog(request.POST)
        if form.is_valid():
            post.titulo=form.cleaned_data.get('titulo')
            post.subtitulo=form.cleaned_data.get('subtitulo')
            post.author=form.cleaned_data.get('author')
            post.description=form.cleaned_data.get('description')
            post.fecha_creacion=form.cleaned_data.get('fecha_creacion')
            post.save()
            
            return redirect('blog_post')
        else:
            return render(request, 'editarBlog.html',{'form': form, 'post':post})
    
    form_blog= FormBlog(initial={'titulo':post.titulo, 'subtitulo':post.subtitulo,'author':post.author,'description':post.description, 'fecha_creacion':post.fecha_creacion})
    
    return render(request, 'editarBlog.html',{'form': form_blog,'post':post})


def eliminar_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blog_post')
