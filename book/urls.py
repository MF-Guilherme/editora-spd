from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.book_register, name='book_register'),
    path('', views.book_index, name='index')
]
