from django.contrib import admin
from .models import Categoria, Producto
from django.utils.safestring import mark_safe

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','producto_count', 'disponible', 'nro_orden')
    list_filter = ('disponible',)
    search_fields = ('nombre',)
    ordering = ('nro_orden', 'nombre')
    def imagen(self, obj):
        if obj.imagen:
            return mark_safe('<img src="%s" width="50" height="50"/>' % obj.imagen.url)
        return "Sin imagen"
    imagen.short_description = 'Vista previa'
    def producto_count(self, obj):
        return obj.productos.count()
    producto_count.short_description = 'N° de productos'
    
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'precio', 'precio_formateado', 'disponible', 'categoria')
    #prepopulated_fields = {'slug': ('nombre',)}  # Genera slug automáticamente
    list_filter = ('disponible', 'categoria')
    search_fields = ('nombre',)
    list_editable = ('precio', 'disponible')
    ordering = ('categoria__nombre', 'nombre', 'precio')
    
    def imagen(self, obj):
        if obj.imagen:
            return mark_safe('<img src="%s" width="50" height="50"/>' % obj.imagen.url)
        return "Sin imagen"
    imagen.short_description = 'Vista previa'
    
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'descripcion','categoria')
        }),
        ('Precio y disponibilidad', {
            'fields': ('precio', 'disponible')
        }),
        ('Imagen del producto', {
            'fields': ('imagen',)
        }),
    )
    
    def precio_formateado(self, obj):
        return f"${obj.precio}"
    precio_formateado.short_description = 'Precio'
    precio_formateado.admin_order_field = 'precio' # Permite ordenar por precio al hacer clic en el encabezado de la columna