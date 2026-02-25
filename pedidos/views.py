from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from menu.models import Producto, VarianteProducto

def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        variante_id = request.POST.get('variante_id')
        cantidad = int(request.POST.get('cantidad', 1))
        
        # Obtener productos y variantes
        producto = get_object_or_404(Producto, id=producto_id, disponible=True)
        variante = None
        precio_unitario = producto.precio

        if variante_id:
            variante = get_object_or_404(VarianteProducto, id=variante_id, disponible=True)
            precio_unitario = producto.precio_total()

        # Inicializar carrito en sesión si no existe
        if 'carrito' not in request.session:
            request.session['carrito'] = {}
        
        carrito = request.session['carrito']

        item_key = str(producto_id)
        if variante_id:
            item_key += f"_{variante_id}"

        # 


    return redirect('inicio')