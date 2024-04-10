from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.author_register, name='author_register'),
    path('', views.author_index, name='index')
]
