from django.shortcuts import render, HttpResponse,redirect
from usuarios.models import Usuario

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario']).nome
        return HttpResponse(f'Ola {usuario}')
    else:
        return redirect('/auth/login/?status=2')
