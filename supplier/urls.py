from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.supplier_register, name='supplier_register'),
    path('', views.supplier_index, name='index')
]
