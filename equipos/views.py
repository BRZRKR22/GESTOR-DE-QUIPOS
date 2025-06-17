# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import RegistroForm
from .models import Equipo

def pagina_inicio(request):
    return render(request, 'equipos/inicio.html')

def principal(request):
    return render(request,'principal.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect('redirect_post_login')
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = RegistroForm()
    return render(request, 'equipos/registro.html', {'form': form})

@login_required
def redirect_post_login(request):
    user = request.user
    if user.is_superuser:
        return redirect('/admin/')
    elif user.groups.filter(name='administrador').exists():
        return redirect('inventario_admin')
    elif user.groups.filter(name='usuario').exists():
        return redirect('inventario')
    else:
        logout(request)
        return redirect('login')

@login_required
def inventario(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/inventario.html', {'equipos': equipos})

@login_required
@permission_required('equipos.view_equipo', raise_exception=True)
def inventario_admin(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/inventario_admin.html', {'equipos': equipos})

@login_required
@permission_required('equipos.add_equipo', raise_exception=True)
def agregar_equipo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        memoria_ram = request.POST.get('memoria_ram')
        almacenamiento = request.POST.get('almacenamiento')
        monitor = request.POST.get('monitor')
        raton = request.POST.get('raton')
        sistema_operativo = request.POST.get('sistema_operativo')
        estado = request.POST.get('estado')  # Captura el estado

        if not all([nombre, memoria_ram, almacenamiento, monitor, raton, sistema_operativo, estado]):
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'equipos/agregar_equipo.html')

        Equipo.objects.create(
            nombre=nombre,
            memoria_ram=memoria_ram,
            almacenamiento=almacenamiento,
            monitor=monitor,
            raton=raton,
            sistema_operativo=sistema_operativo,
            estado=estado  # Asignar estado
        )
        messages.success(request, "Equipo agregado correctamente.")
        return redirect('inventario_admin')

    return render(request, 'equipos/agregar_equipo.html')

@login_required
@permission_required('equipos.change_equipo', raise_exception=True)
def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        equipo.nombre = request.POST.get('nombre')
        equipo.memoria_ram = request.POST.get('memoria_ram')
        equipo.almacenamiento = request.POST.get('almacenamiento')
        equipo.monitor = request.POST.get('monitor')
        equipo.raton = request.POST.get('raton')
        equipo.sistema_operativo = request.POST.get('sistema_operativo')
        equipo.estado = request.POST.get('estado')  # Actualizar estado
        equipo.save()
        messages.success(request, "Equipo actualizado correctamente.")
        return redirect('inventario_admin')

    return render(request, 'equipos/editar_equipo.html', {'equipo': equipo})

@login_required
@permission_required('equipos.delete_equipo', raise_exception=True)
def eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, "Equipo eliminado correctamente.")
        return redirect('inventario_admin')
    return render(request, 'equipos/eliminar_equipo.html', {'equipo': equipo})
