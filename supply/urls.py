from django.urls import path
from . import views

app_name = 'supply'

urlpatterns = [
    path('supplier_register/', views.supplier_register, name='register'),
    path('', views.supplier_index, name='index')
]
