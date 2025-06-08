
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import Producto

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inventario')
    else:
        form = RegistroForm()
    return render(request, 'inventario/registro.html', {'form': form})

@login_required
def inventario(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/inventario.html', {'productos': productos})
