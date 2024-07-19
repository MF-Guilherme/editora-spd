from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('books/', views.book_register, name='books'),
    path('author_register/', views.author_register, name='author_register'),
    path('author_register/update/<int:author_id>',
         views.author_update,
         name='author_update'),
    path('author_register/delete/<int:author_id>',
         views.author_delete,
         name='author_delete'),
]
