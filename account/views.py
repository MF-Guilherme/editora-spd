from django.shortcuts import render
from django.http import HttpResponse

def account_register(request):
    return HttpResponse('Account register window')

def account_index(request):
    return HttpResponse('Account index')
