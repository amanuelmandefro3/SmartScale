from django.db import models
from django.utils import timezone

# Create your models here.
class Scale(models.Model):
    name = models.CharField(max_length=250, default="Sample name" )
    expire_date = models.DateTimeField("expiry date", default=timezone.now)
    mass = models.DecimalField(decimal_places=2, max_digits=10)

    # def __str__(self) -> str:
    #     return f'{self.name} {self.expire_date}'