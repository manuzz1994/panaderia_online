from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle, name='detalle_producto'),
]