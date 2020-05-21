from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    email = models.EmailField()

    def __str__(self):
        return self.name + '(' + self.gender + ')'

class Driver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=1)
    dpi = models.IntegerField()

    def __str__(self):
        return self.name + '(' + self.gender + ')' + ', ' + self.email
