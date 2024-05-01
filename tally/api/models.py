from django.db import models
from drinks.models import Drink

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Tally(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="tally")
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="tally")
    created_at = models.DateTimeField(auto_now_add=True)