from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import RegistroForm
from .models import Equipo

def pagina_inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('redirect_post_login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def redirect_post_login(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    elif request.user.groups.filter(name='administrador').exists():
        return redirect('inventario_admin')
    else:
        return redirect('inventario')

@login_required
def inventario(request):
    equipos = Equipo.objects.all()
    return render(request, 'inventario.html', {'equipos': equipos})

@login_required
@permission_required('equipos.change_equipo', raise_exception=True)
def inventario_admin(request):
    equipos = Equipo.objects.all()
    return render(request, 'inventario_admin.html', {'equipos': equipos})

@login_required
@permission_required('equipos.add_equipo', raise_exception=True)
def agregar_equipo(request):
    if request.method == 'POST':
        Equipo.objects.create(
            nombre=request.POST['nombre'],
            memoria_ram=request.POST['memoria_ram'],
            almacenamiento=request.POST['almacenamiento'],
            monitor=request.POST['monitor'],
            raton=request.POST['raton'],
            sistema_operativo=request.POST['sistema_operativo']
        )
        return redirect('inventario_admin')
    return render(request, 'agregar_equipo.html')

@login_required
@permission_required('equipos.change_equipo', raise_exception=True)
def editar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    if request.method == 'POST':
        equipo.nombre = request.POST['nombre']
        equipo.memoria_ram = request.POST['memoria_ram']
        equipo.almacenamiento = request.POST['almacenamiento']
        equipo.monitor = request.POST['monitor']
        equipo.raton = request.POST['raton']
        equipo.sistema_operativo = request.POST['sistema_operativo']
        equipo.save()
        return redirect('inventario_admin')
    return render(request, 'editar_equipo.html', {'equipo': equipo})

@login_required
@permission_required('equipos.delete_equipo', raise_exception=True)
def eliminar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('inventario_admin')
    return render(request, 'eliminar_equipo.html', {'equipo': equipo})
