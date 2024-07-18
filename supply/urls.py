from django.urls import path
from . import views
urlpatterns = [
    path('supplier_register/', views.supplier_register, name='supplier_register'),
    path('account_register/', views.account_register, name='account_register'),
    path('', views.supplier_index, name='index')
]
