from django.db import models
from django.utils import timezone

# Options for choices
GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('binary','BINARY'),
)
MARITAL_STATUS_CHOICES = (
    ('single','SINGLE'),
    ('maried', 'MARIED'),
)
SCHEDULE_CHOICES = (
    ('morning','MORNING'),
    ('afternoon', 'AFTERNOON'),
    ('night','NIGHT'),
)

# Creación de campos del modelo 'Empleados' 
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=500)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)
    id_cedula = models.BigIntegerField()
    #date_of_entry = models.DateField()
    date_of_birth = models.DateField()
    language = models.CharField(max_length=255)
    #salary_rate = models.PositiveIntegerField()
    id_harmond = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254) 
    nationality = models.CharField(max_length=255)
    telephone_number = models.BigIntegerField()
    #training_hours = models.BigIntegerField()
    #address = models.CharField(max_length=255)
    #referal_name = models.CharField(max_length=255)
    #project_team = models.CharField(max_length=255)
    #time_in_company = models.DateField()
    #vacations_available = models.PositiveIntegerField()
    #last_day_at_company = models.DateField()
    #notes = models.TextField(null=True)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=25)
    #bank_account_number = models.PositiveIntegerField()
    schedule = models.CharField(choices=SCHEDULE_CHOICES, max_length=25)
    picture = models.ImageField()
    updated = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return self.full_name + self.id_harmond

    class Meta:
         db_table = 'Employees' 
         # Le doy de nombre 'Empleados' 
         # a nuestra tabla en la Base de Datos