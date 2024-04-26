from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.first_name + self.last_name

class Drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Tally(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
