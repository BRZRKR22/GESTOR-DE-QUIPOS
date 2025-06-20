from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('redirect_post_login/', views.redirect_post_login, name='redirect_post_login'),
    path('inventario/', views.inventario, name='inventario'),
    path('inventario_admin/', views.inventario_admin, name='inventario_admin'),
    path('agregar_equipo/', views.agregar_equipo, name='agregar_equipo'),
    path('editar_equipo/<int:equipo_id>/', views.editar_equipo, name='editar_equipo'),
    path('eliminar_equipo/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('principal/', views.principal, name='principal'),
]
