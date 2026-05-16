from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('articulo/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('articulo/crear/', views.crear_articulo, name='crear_articulo'),
    path('articulo/<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),
    path('articulo/<int:pk>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
]
