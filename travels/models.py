from django.db import models
from users.models import Client, Driver

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name + '(' + str(self.price) + ')'

class Vehicle(models.Model):
    color = models.CharField(max_length=25)
    plates = models.CharField(max_length=7)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand + ', ' + self.model + ', ' + self.plates + '(' + self.color + ')'

class Travel(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return self.client + ', ' + self.vehicle + '(' + self.destination + ')'
