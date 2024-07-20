from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Book, Author
from django.http import HttpResponse  # noqa


def author_register(request):
    if request.method == 'GET':
        authors = Author.objects.all().order_by('-id')
        return render(request, 'authors.html', {'authors': authors})
    elif request.method == 'POST':
        name = request.POST.get('author-name')
        author = Author(name=name)
        author.save()
        messages.success(request, "Autor cadastrado com sucesso!")
        return redirect('/library/authors')


def author_update(request, author_id):
    if request.method == 'GET':
        author = Author.objects.filter(id=author_id).first()
        return render(request, 'author_update.html', {'author': author})
    elif request.method == 'POST':
        author = Author.objects.filter(id=author_id).first()
        new_author = request.POST.get('author-name')
        author.name = new_author
        author.save()
        messages.success(request, 'Autor atualizado com sucesso!')
        return redirect('/library/authors')


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
        return redirect('/library/authors')


def book_register(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('-id')
        authors = Author.objects.all().order_by('name')
        return render(request, 'books.html', {'authors': authors, 'books': books}) # noqa
    elif request.method == 'POST':
        author_id = int(request.POST.get('author'))
        pub_at = request.POST.get('year-publication')
        book = Book(author_id=author_id, published_at=pub_at)
        book.save()
        messages.success(request, 'Livro cadastrado com sucesso!')
        return redirect('/library/books')


def book_update(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(id=book_id)
        authors = Author.objects.all().order_by('name')
        return render(request, 'book_update.html', {'book': book, 'authors': authors}) # noqa
    elif request.method == 'POST':
        try:
            book = Book.objects.get(id=book_id)
            new_author = request.POST.get('author')
            new_pub = request.POST.get('year-publication')
            book.author_id = int(new_author)
            book.published_at = new_pub
            book.full_clean()
            book.save()
            messages.success(request, 'Livro atualizado com sucesso!')
        except ValidationError as e:
            error_message = e.message_dict.get('published_at', ["Erro desconhecido"])[0] # noqa
            messages.error(request, error_message)
        finally:
            return redirect('/library/books')


def book_delete(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(id=book_id)
        messages.warning(request,
                         'Deseja excluir permanentemente o livro abaixo?')
        return render(request, 'book_delete.html', {'book': book})
    elif request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('/library/books/')
