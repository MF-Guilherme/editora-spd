from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('book_register/', views.book_register, name='book_register'),
    path('author_register/', views.author_register, name='author_register'),
    path('', views.library_index, name='index')
]
