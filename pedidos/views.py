from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from menu.models import Producto, VarianteProducto

def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        variante_id = request.POST.get('variante_id')
        cantidad = int(request.POST.get('cantidad', 1))
        
        # Aquí irá la lógica del carrito (usando sesiones)
        messages.success(request, f"Producto agregado (simulación)")
        
    return redirect('inicio')