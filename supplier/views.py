from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'suppliers.html')

def register(request):
    return render(request, 'register_supplier.html')
