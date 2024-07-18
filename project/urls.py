from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suppliers/', include('supply.urls')),
    path('library/', include('library.urls')),
    path('assembly/', include('automaker.urls')),

]
