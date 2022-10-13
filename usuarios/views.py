import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256

# Create your views here.
def login(request):
    status = request.GET.get('status')
    return render(request, 'usuarios/login.html', {'status' : status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'usuarios/cadastro.html',{'status' : status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    #Pegar todos os usuarios para fazer as verificacoes
    usuario = Usuario.objects.filter(email=email)
    

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    #Verificar se a senha tem menos do que 8 caracteres
    if len(senha) < 6:
        return redirect('/auth/cadastro/?status=2')

    #verificar se o email já existe no banco de dados
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome , email = email, senha = senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()
    
    usuario = Usuario.objects.filter(email=email, senha=senha)
    #print(request.session['usuario'])
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        print(request.session['usuario'])

        return redirect('/livros/home')    

    return HttpResponse(f'{email} {senha}')

def sair(request):
     request.session.flush()
     return redirect('/auth/login/')