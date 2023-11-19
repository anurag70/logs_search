from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('log/',include('logingest.urls')),
    path('admin/', admin.site.urls),
]