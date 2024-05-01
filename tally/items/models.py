from django.db import models
from drinks.models import Drink
from api.models import Person

# Create your models here.
class Tally(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="tally")
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="tally")
    created_at = models.DateTimeField(auto_now_add=True)