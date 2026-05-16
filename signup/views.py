from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroForm


def registro(request):
    if request.user.is_authenticated:
        return redirect('lista_articulos')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}! Tu cuenta ha sido creada.')
            return redirect('lista_articulos')
    else:
        form = RegistroForm()
    return render(request, 'signup/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('lista_articulos')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido de nuevo, {user.username}!')
            next_url = request.POST.get('next') or request.GET.get('next') or 'lista_articulos'
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'signup/login.html', {
        'next': request.GET.get('next', ''),
    })


def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('lista_articulos')
