from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blog.forms import FormBlog,BusquedaAuthor
from blog.models import Blog

# Create your views here.


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def lista_post(request):
    
    busqueda=request.GET.get('author')
    
    if busqueda:
        listado = Blog.objects.filter(author__icontains=busqueda)
    else:
        listado = Blog.objects.all()
    
    posts = BusquedaAuthor()
    return render(request, 'blogPost.html', {'posts': posts, 'listado': listado})

@login_required
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

@login_required
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

@login_required
def eliminar_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blog_post')

@login_required
def mostrar_blog(request, id):
    form = Blog.objects.get(id=id)
    return render(request, 'mostrar_blog.html', {'form': form})

