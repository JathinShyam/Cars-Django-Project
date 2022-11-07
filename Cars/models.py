
from django.db import models


class Car(models.Model):
    CarName= models.CharField(max_length=20)
    mpg= models.DecimalField(decimal_places=2, max_digits=5)
    cyl= models.IntegerField()
    disp= models.DecimalField(decimal_places=2, max_digits=5)
    hp= models.IntegerField()
    drat= models.DecimalField(decimal_places=2, max_digits=5)
    wt= models.DecimalField(decimal_places=2, max_digits=5)
    qsec= models.DecimalField(decimal_places=2, max_digits=5)
    vs= models.IntegerField()
    am= models.IntegerField()
    gear= models.IntegerField()
    carb= models.IntegerField()
    
    def __str__ (self):
        
        return self.CarName
