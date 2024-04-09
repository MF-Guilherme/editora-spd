from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.account_register, name='account_register'),
    path('', views.account_index, name='index')
]
