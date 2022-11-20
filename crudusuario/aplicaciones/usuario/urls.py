from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('registrarUsuario/', views.registrarUsuario),
    path('eliminarUsuario/<codigo>', views.eliminarUsuario),
    path('asignaturas/edicionUsuario/<codigo>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('asignaturas/', views.asignaturas)
    ]
    