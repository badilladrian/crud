# crud
This is a django project for the creation, reading, updating and deleting of employees-

Use this URLs to access each module:
 
   'employees/details/<int:pk>'
    EmployeeDetails display
     
   'employees/create'
   EmployeeCreate function
 
   'employees/update/<int:pk>'
   EmployeeUpdate function
 
   'employees/delete/<int:pk>'
   EmployeeDelete function


If url='', then welcome.html displayed-
----------------------------**------------------------------


[packages]
requests = "*"
django = "*"
psycopg2 = "*"
mysqlclient = "*"
pillow = "*"
django-bootstrap4 = "*"
django-widget-tweaks = "*"

[requires]
python_version = "3.8"
