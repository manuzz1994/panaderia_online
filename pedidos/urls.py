from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
]