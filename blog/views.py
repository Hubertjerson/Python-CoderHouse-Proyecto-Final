from datetime import datetime
from django.shortcuts import redirect, render

from blog.forms import FormBlog
from blog.models import Blog
# Create your views here.


def about(request):
    return render(request,'about.html')


def home(request):
    return render(request, 'home.html')


def blog_post(request):
    posts = Blog.objects.all()
    return render(request, 'blogPost.html', {'posts': posts})


def blog_get(request):

    if request.method == 'POST':
        form = FormBlog(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now()

            post_public = Blog(
                title=data.get('title'),
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
