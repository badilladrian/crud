from django.urls import path
from .views import *

#Always import the views to the URL area

urlpatterns = [
    # La ruta 'employees' en donde listamos todos los employees
    path('list/', EmployeeList.as_view(template_name = "crud/list.html"), name='list'),
 
    # La ruta 'details' en donde mostraremos una página con los detalles de un employee
    path('details/<int:pk>', EmployeeDetail.as_view(template_name = "crud/details.html"), name='details'),
 
    # La ruta 'create' en donde mostraremos un formulario para crear un nuevo employee
    path('create/', EmployeeCreate.as_view(template_name = "crud/create.html"), name='create'),
 
    # La ruta 'update' en donde mostraremos un formulario para actualizar un employee
    path('update/<int:pk>', EmployeeUpdate.as_view(template_name = "crud/update.html"), name='update'), 
 
    # La ruta 'delete' que usaremos para eliminar un employee
    path('delete/<int:pk>', EmployeeDelete.as_view(), name='delete'),    

]

