from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Supplier


def supplier_index(request):
    return render(request, 'suppliers.html')


def supplier_register(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all().order_by('name')
        return render(request, 'supplier_register.html', {'suppliers': suppliers})
    elif request.method == 'POST':    
        name = request.POST.get('name')
        supplier = Supplier(name=name)
        supplier.save()
        print('cadastro efetuado com sucesso')
        return redirect("/suppliers/")


def account_register(request):
    return HttpResponse('Account register window')


def account_index(request):
    return HttpResponse('Account index')
