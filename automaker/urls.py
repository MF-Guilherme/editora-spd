from django.urls import path
from . import views

app_name = 'automaker'

urlpatterns = [
    path('', views.assembly_register, name='assembly'),
]
