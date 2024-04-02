from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Supplier index window')

def register(request):
    return HttpResponse('Supplier register window')
