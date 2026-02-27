from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    
    path('actualizar/', views.actualizar_carrito, name='actualizar_carrito'),
    
    path('eliminar/<str:item_key>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    
    path('checkout/', views.checkout, name='checkout'),
    
    path('confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
]