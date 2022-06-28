from django.db import models

# Create your models here.
class House(models.Model):
    bathroom = models.IntegerField()
    bedroom = models.IntegerField()
    garden = models.IntegerField()
    garage = models.IntegerField()
    parking = models.IntegerField()
    pet = models.BooleanField(default=False, blank=False, null=False)
    pool = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.bathroom