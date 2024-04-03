from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse('Account register window')

def index(request):
    return HttpResponse('Account index')
