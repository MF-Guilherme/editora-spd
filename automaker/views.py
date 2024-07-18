from django.shortcuts import render


def assembly_register(request):
    return render(request, 'assemblies.html')
