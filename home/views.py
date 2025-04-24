from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def home_view(request):
    return render(
        request,
        'index.html'
    )

def register_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        pass1 = data.get('password1')
        pass2 = data.get('password2')
        email = data.get('email')
        
        if not username or not pass1 or not pass2:
            messages.error(request, "faltan datos")
        
        elif _validate_pass(pass1, pass2):
            messages.error(request, "las contraseñas no coinciden")
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "el usuario esta en uso")
        
        else:
            User.objects.create_user(
                username=username, 
                password=pass1,
                email=email
            )
    return render(
        request=request,
        template_name='accounts/register.html'
    )

def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password) #autentica pero no lo loguea, si encuentra lo retorna true sino false
    
        if user is not None:
            login(request, user)   #esto si hace que nuestro usuario este logueado
            messages.success(request, "Sesion Iniciada")
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            
    return render(
        request,
        template_name='accounts/login.html'
    )

def logout_view(request):
    logout(request)
    return redirect('login')

#van al final todos los metodos privados
def _validate_pass(pass1, pass2):
    print(pass1==pass2)
    pass1 == pass2