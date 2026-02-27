from django.shortcuts import redirect, get_object_or_404, render
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
            precio_unitario = variante.precio_total()

        # Inicializar carrito en sesión si no existe
        if 'carrito' not in request.session:
            request.session['carrito'] = {}
        
        carrito = request.session['carrito']

        # Crear clave única para el producto (y variante si existe)
        item_key = str(producto_id)
        if variante_id:
            item_key += f"_{variante_id}"

        # Si el item ya existe, sumar y actualizar
        if item_key in carrito:
            carrito[item_key]['cantidad'] += cantidad
            carrito[item_key]['subtotal'] = carrito[item_key]['cantidad'] * carrito[item_key]['precio_unitario']
        else:
            carrito[item_key] = {
                'producto_id': producto.id,
                'producto_nombre': producto.nombre,
                'variante_id': variante.id if variante else None,
                'variante_nombre': variante.nombre if variante else None,
                'precio_unitario': float(precio_unitario),
                'subtotal': float(cantidad * precio_unitario),
                'cantidad': cantidad,
            }
            
        # Guardar sesion
        request.session['carrito'] = carrito
        request.session.modified = True
        
        messages.success(request, f"{producto.nombre} agregado al carrito.")

    return redirect('inicio')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    
    #calcular total
    total = 0
    for item in carrito.values():
        total += item['subtotal']
        
    return render(request, 'pedidos/carrito.html', {'carrito': carrito, 'total': total})

def actualizar_carrito(request):
    if request.method == 'POST':
        item_key = request.POST.get('item_key')
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        
        carrito = request.session.get('carrito', {})
        
        if item_key in carrito:
            if nueva_cantidad > 0:
                carrito[item_key]['cantidad'] = nueva_cantidad
                carrito[item_key]['subtotal'] = nueva_cantidad * carrito[item_key]['precio_unitario']
                messages.success(request, "Cantidad actualizada.")
            else:
                del carrito[item_key]
                messages.success(request, "Producto eliminado del carrito.")
            
            request.session['carrito'] = carrito
            request.session.modified = True
    return redirect('ver_carrito')

def eliminar_del_carrito(request, item_key):
    carrito = request.session.get('carrito', {})
    if item_key in carrito:
        del carrito[item_key]
        request.session['carrito'] = carrito
        request.session.modified = True
        messages.success(request, "Producto eliminado del carrito.")
    return redirect('ver_carrito')

def checkout(request):
    carrito = request.session.get('carrito', {})
    
    if not carrito:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')
    
    total = sum(item['subtotal'] for item in carrito.values())
    
    # Aquí iría la lógica para procesar el pago y crear la orden
    return render(request, 'pedidos/checkout.html', {'carrito': carrito, 'total': total})

def confirmar_pedido(request):
    if request.method == 'POST':
        # Por ahora solo mostrar mensaje de éxito
        metodo_entrega = request.POST.get('metodo_entrega')
        metodo_pago = request.POST.get('metodo_pago')
        telefono = request.POST.get('telefono')
        
        messages.success(request, f"¡Pedido confirmado! Nos pondremos en contacto contigo al {telefono}.")
        
        # Limpiar carrito
        request.session['carrito'] = {}
        request.session.modified = True
        
        return redirect('inicio')
    
    return redirect('ver_carrito')