from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Login y logout
    path('', include('inventario.urls')),  # URLs de la app inventario
]
