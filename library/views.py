from django.shortcuts import render
# from django.http import HttpResponse


def library_index(request):
    return render(request, 'books.html')


def book_register(request):
    return render(request, 'book_register.html')


def author_register(request):
    return render(request, 'author_register.html')
