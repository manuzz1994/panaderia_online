from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible?")
    nro_orden = models.IntegerField(default=0, verbose_name="Número de orden")
    #SLUG: slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    #Metedo para SLUG= def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug = slugify(self.nombre)
    #    super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"
        ordering = ['nro_orden', 'nombre', 'disponible']


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del producto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible?")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen del producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    #creado = models.DateTimeField(auto_now_add=True)
    #actualizado = models.DateTimeField(auto_now=True)
    #SLUG: slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    #Metodo para SLUG= def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug = slugify(self.nombre)
    #    super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['categoria__nombre', 'nombre', 'precio', 'disponible']
    