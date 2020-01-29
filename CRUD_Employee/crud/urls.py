from django.urls import path
from .views import *

#Always import the views to the URL area

urlpatterns = [
    # La ruta 'leer' en donde listamos todos los registros o employees de la Base de Datos
    path('employees/', EmployeeList.as_view(template_name = "employees/index.html"), name='list'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un employees o registro 
    path('employees/details/<int:pk>', EmployeeDetail.as_view(template_name = "employees/detalles.html"), name='details'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo employees o registro  
    path('employees/create', EmployeeCreate.as_view(template_name = "employees/crear.html"), name='create'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un employees o registro de la Base de Datos 
    path('employees/update/<int:pk>', EmployeeUpdate.as_view(template_name = "employees/actualizar.html"), name='update'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un employees o registro de la Base de Datos 
    path('employees/delete/<int:pk>', EmployeeDelete.as_view(), name='delete'),    

]

