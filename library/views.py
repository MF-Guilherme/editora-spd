from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author
# from django.http import HttpResponse


def library_index(request):
    return render(request, 'books.html')


def book_register(request):
    return render(request, 'book_register.html')


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
