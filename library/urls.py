from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('authors/', views.author_register, name='authors'),
    path('authors/update/<int:author_id>', views.author_update, name='author_update'), # noqa
    path('authors/delete/<int:author_id>', views.author_delete, name='author_delete'), # noqa
    path('books/', views.book_register, name='books'),
    path('books/update/<int:book_id>', views.book_update, name='book_update'),
    path('books/delete/<int:book_id>', views.book_delete, name='book_delete'),
]
