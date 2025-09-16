# Ex02 Django ORM Web Application
## Date: 16.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_no=models.IntegerField(primary_key=True)
    car_model=models.CharField(max_length=20)
    date_of_manufacture=models.DateField()
    fuel_type=models.CharField(max_length=10)
    Years_of_warranty=models.IntegerField()
class CarAdmin(admin.ModelAdmin):
    list_display=["car_no","car_model","date_of_manufacture","fuel_type","Years_of_warranty"]

admin.py

from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car,CarAdmin)

```

## OUTPUT

![alt text](<Screenshot (1).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
