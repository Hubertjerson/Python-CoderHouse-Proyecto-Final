from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as Login, authenticate
from django.contrib.auth.decorators import login_required

from accounts.models import MasDatosUsuario
from .forms import MyUserCreationForm, MyUserEditForm

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
                return render(request, "home.html" )
            else:
                return render(request, 'accounts/login.html', {'form':form})

        else:
            return render(request, 'accounts/login.html', {'form':form})

    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})

def register (request): 
    if request.method == 'POST':

        form = MyUserCreationForm(request.POST,request.FILES)
        #usuario_extendido, _ = NuestroUser.objects.get_or_create(user=request.user)

        if form.is_valid():
            #user = usuario_extendido(imagen=form.cleaned_data['imagen'])
            #user.save()
            username = form.cleaned_data['username']
            form.save()
            return render(request, "home.html", {'msj':f'Se creo el user {username}'})
        else:
            return render(request, "accounts/register.html", {'form':form})
    form = MyUserCreationForm()
    return render(request, "accounts/register.html", {'form':form})

@login_required
def editar (request):
    
    user = request.user
    mas_datos_usuario, _= MasDatosUsuario.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
                
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuario.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuario.avatar
            
            # if data.get('password1') and data.get('password1') == data.get('password2'):
            #     user.set_password(data.get('password1'))
            
            mas_datos_usuario.save()
            user.save()
    
            return render(request, 'accounts/perfil.html')
        
        else:
            return render(request, 'accounts/editar_user.html', {'form': form})
            
    form = MyUserEditForm(
            initial={
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'avatar': mas_datos_usuario.avatar
            }
        )

    return render(request, 'accounts/editar_user.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')