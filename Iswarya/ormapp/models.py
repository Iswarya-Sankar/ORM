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
