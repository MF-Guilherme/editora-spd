from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author
from django.http import HttpResponse


def library_index(request):
    return render(request, 'books.html')


def author_register(request):
    if request.method == 'GET':
        authors = Author.objects.all().order_by('-id')
        return render(request, 'author_register.html', {'authors': authors})
    elif request.method == 'POST':
        name = request.POST.get('author-name')
        author = Author(name=name)
        author.save()
        messages.success(request, "Autor cadastrado com sucesso!")
        return redirect('/library/author_register')


def author_update(request, author_id):
    if request.method == 'GET':
        author = Author.objects.filter(id=author_id).first()
        return render(request, 'author_update.html', {'author': author})
    elif request.method == 'POST':
        author = Author.objects.filter(id=author_id).first()
        new_author = request.POST.get('author-name')
        author.name = new_author
        author.save()
        messages.success(request, 'Nome do autor atualizado com sucesso!')
        return redirect('/library/author_register')


def author_delete(request, author_id):
    if request.method == 'GET':
        author = Author.objects.filter(id=author_id).first()
        messages.warning(request,
                         'Deseja excluir permanentemente o autor abaixo?')
        return render(request, 'author_delete.html', {'author': author})
    elif request.method == 'POST':
        author = Author.objects.filter(id=author_id).first()
        author.delete()
        messages.success(request, 'Autor excluído com sucesso')
        return redirect('/library/author_register')


def book_register(request):
    return render(request, 'book_register.html')
