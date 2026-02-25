from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto, VarianteProducto

def inicio(request):
    """Vista para mostrar la página de inicio con las categorías disponibles."""
    categorias = Categoria.objects.filter(disponible=True).order_by('nro_orden', 'nombre')
    return render(request, 'menu/inicio.html', {'categorias': categorias})

def productos_por_categoria(request, categoria_id):
    """Vista para mostrar los productos de una categoría específica."""
    categoria = get_object_or_404(Categoria, id=categoria_id, disponible=True)
    productos = categoria.productos.filter(disponible=True).order_by('nombre')
    return render(request, 'menu/categoria.html', {'categoria': categoria, 'productos': productos})

def detalle(request, producto_id):
    """Vista para mostrar el detalle de un producto específico y sus variantes."""
    producto = get_object_or_404(Producto, id=producto_id, disponible=True)
    variantes = producto.variantes.filter(disponible=True).order_by('nombre')
    return render(request, 'menu/detalle.html', {'producto': producto, 'variantes': variantes})
    

# Create your views here.
