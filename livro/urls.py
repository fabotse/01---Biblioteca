from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.livros, name='livros'),
    path('livro/<str:id>', views.livro, name='livro'),
    path('cadastrar_livro', views.cadastrar_livro, name='cadastrar_livro')
]
