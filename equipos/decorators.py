from django.shortcuts import redirect
from .models import Perfil

def rol_requerido(roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            perfil = Perfil.objects.get(user=request.user)
            if perfil.rol not in roles:
                return redirect('inventario')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
