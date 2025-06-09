from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración
    path('accounts/', include('django.contrib.auth.urls')),  # Login/logout
    path('', include('equipos.urls')),  # URLs de nuestra app
]
