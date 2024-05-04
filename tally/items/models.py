from django.db import models
from django.conf import settings

from drinks.models import Drink
from api.models import Person

User = settings.AUTH_USER_MODEL

# Create your models here.
class TallyItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="tally")
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="tally")
    created_at = models.DateTimeField(auto_now_add=True)