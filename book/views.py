from django.shortcuts import render
from django.http import HttpResponse

def book_index(request):
    return HttpResponse('books index')


def book_register(request):
    return HttpResponse('books register')

