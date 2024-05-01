from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name