from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Supplier, Account


def supplier_register(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all().order_by('name')
        return render(
            request,
            'suppliers.html', {'suppliers': suppliers}
            )
    elif request.method == 'POST':
        name = request.POST.get('name')
        supplier = Supplier(name=name)
        supplier.save()
        messages.success(request, 'Fornecedor cadastrado com sucesso!')
        return redirect("/suppliers/")
