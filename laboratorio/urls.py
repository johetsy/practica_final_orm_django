from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('listar', views.listar_lab, name='listar_lab'),
    path('insertar/', views.insertar_lab, name='insertar_lab'),
    path('editar/<int:laboratorio_id>/', views.editar_lab, name='editar_lab'),
    path('eliminar/<int:laboratorio_id>/', views.eliminar_lab, name='eliminar_lab'),
]