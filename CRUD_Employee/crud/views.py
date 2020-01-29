from django.shortcuts import render
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
# Importamos los modelos del APP
from .models import *
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
# Habilitamos los formularios en Django
from django import forms

#Form que muestra lista de los objetos modelo existentes
class EmployeeList(ListView): 
    model = Employee

class EmployeeCreate(SuccessMessageMixin, CreateView): 
    model = Employee # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Employee # Definimos nuestro formulario con el nombre de la clase o modelo 'Employee'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Employee' de nuestra Base de Datos 
    success_message = 'Employee Correctly Created !' # Mostramos este Mensaje luego de Crear un Employee

    # Redireccionamos a la página principal luego de crear un registro o Employee
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
#Form que muestra los detalles del modelo
class EmployeeDetail(DetailView): 
    model = Employee

class EmployeeUpdate(SuccessMessageMixin, UpdateView): 
    model = Employee # Llamamos a la clase 'Employee' que se encuentra en nuestro archivo 'models.py' 
    form = Employee # Definimos nuestro formulario con el nombre de la clase o modelo 'Employee' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Employee' de nuestra Base de Datos 
    success_message = 'Employee Updated !' # Mostramos este Mensaje luego de Editar un Employee 
 
    # Redireccionamos a la página principal luego de actualizar un registro o Employee
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class EmployeeDelete(SuccessMessageMixin, DeleteView): 
    model = Employee 
    form = Employee
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Employee
    def get_success_url(self): 
        success_message = 'Employee Deleted !' # Mostramos este Mensaje luego de Editar un Employee 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


