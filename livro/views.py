from django.shortcuts import render, HttpResponse,redirect
from usuarios.models import Usuario
from .models import Categoria, Livro, Emprestimo
from .forms import LivroForm
# Create your views here.

def livros(request):
    status = request.GET.get('status')
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        form = LivroForm()
        
        livros = Livro.objects.filter(usuario = usuario)
        form.fields['usuario'].initial = usuario.id
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        context = {'livros' : livros, 'usuario' : usuario, 'status':status, 'usuario_logado' : request.session.get('usuario'), 'form' : form}

        return render(request, 'livros/livros.html', context)
    else:
        return redirect('/auth/login/?status=2')

def livro(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livro = Livro.objects.get(id=id)
        #Verificando se o usuario é o dono do livro
        #print(request.session.get('usuario'))
        #print(livro.usuario.id)
        if request.session.get('usuario') == livro.usuario.id:
            form = LivroForm()
            categoria_livro = Categoria.objects.filter(usuario=request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro = livro)
            form.fields['usuario'].initial = usuario.id
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            context = {'livro' : livro, 'categoria_livro':categoria_livro, 'emprestimos' : emprestimos, 'usuario_logado' : request.session.get('usuario'), 'form' : form}
            return render(request, 'livro/livro.html', context)
        else:
            return redirect('/livros/?status=3')
    else:
        return redirect('/auth/login/?status=2')            

def cadastrar_livro(request):
    if request.method=="POST":
        form = LivroForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/livros/?status=4')
        
        return redirect('/livros/?status=5')