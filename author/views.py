from django.shortcuts import render
from django.http import HttpResponse


def author_index(request):
    return HttpResponse('Author Index')


def author_register(request):
    return HttpResponse('Author Register')

