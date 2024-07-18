from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('book_register/', views.book_register, name='book_register'),
    path('author_register/', views.author_register, name='author_register'),
    path('author_register/update/<int:author_id>',
         views.author_update,
         name='author_update'),
    path('', views.library_index, name='index')
]
