from django.db import models

# Create your models here.
# myproject/cars/models.py
from django.db import models

class Sell(models.Model):
    carname = models.CharField(max_length=100)
    caryear = models.PositiveIntegerField()
    carseats = models.PositiveIntegerField()
    carfuel = models.CharField(max_length=10)
    carmileage = models.PositiveIntegerField()
    quote_price = models.PositiveIntegerField()
    def __str__(self):
        return self.carname
    
class Selling(models.Model):
    manufacturer_name = models.CharField(max_length=100)
    manufacture_year = models.PositiveIntegerField()
    number_of_seats = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=10)
    mileage = models.PositiveIntegerField()
    quote_price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.manufacturer_name} - {self.manufacture_year}"


 