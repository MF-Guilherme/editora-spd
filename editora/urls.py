from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suppliers/', include('supplier.urls')),
    path('accounts/', include('account.urls')),
    path('authors/', include('author.urls')),
    path('books/', include('book.urls')),
]
