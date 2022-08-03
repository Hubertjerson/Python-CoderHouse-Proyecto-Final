from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as Login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import FormRegister, FormEditUser
from .models import NuestroUser

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not  None:
                Login(request, user)
                usuario = form.cleaned_data['username']
                return render(request, "home.html" )
            else:
                return render(request, 'accounts/login.html', {'form':form,'msj':f'Bienvenido {usuario}!'})

        else:
            return render(request, 'accounts/login.html', {'form':form})

    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})

def register (request):
    if request.method == 'POST':

        form = FormRegister(request.POST,request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "home.html",{'msj':f'Se creo el user {username}'})
        else:
            return render(request, "accounts/register.html", {'form':form,})
    form = FormRegister()
    return render(request, "accounts/register.html", {'form':form})

@login_required
def editar (request):
    
    usuario_extendido, _= NuestroUser.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = FormEditUser(request.POST, request.FILES)

        if form.is_valid():

            data = form.cleaned_data
            logued_user = request.user
            if data.get('first_name'):
                logued_user.first_name = data.get('first_name')
            if data.get('last_name'):
                logued_user.last_name = data.get('last_name')

            logued_user.email= data.get('email') if data.get('email') else logued_user.email
            usuario_extendido.imagen = data.get('imagen') if data.get('imagen') else usuario_extendido.imagen

            usuario_extendido.link= data['link']
            usuario_extendido.bio = data['bio']


            if data.get('password1') == data.get('password2') and len(data.get("password1")) >8:
                logued_user.set_password(data.get('password1'))
                msj = 'se actualizo su contraseña'
            else:
                msj='No se hizo cambios en su contraseña'

            logued_user.save()
            usuario_extendido.save()

            return render(request, "home.html", {'msj':msj})
        else:
            return render(request, "home.html", {'form':form})

    form = FormEditUser(
        initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'imagen': usuario_extendido.imagen,
            'link': usuario_extendido.link,
            'bio': usuario_extendido.bio
        }
    )
    return render(request, "accounts/editar_user.html", {'form':form})

@login_required
def perfil(request):
    mas_datos, _ = NuestroUser.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {'mas_datos':mas_datos})
