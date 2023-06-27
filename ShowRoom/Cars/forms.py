from django import forms
from django.forms import ModelForm
from .models import Car



class CarForm(forms.Form):
    CarName= forms.CharField(max_length=20)
    mpg= forms.DecimalField(decimal_places=2, max_digits=5)
    cyl= forms.IntegerField()
    disp= forms.DecimalField(decimal_places=2, max_digits=5)
    hp= forms.IntegerField()
    drat= forms.DecimalField(decimal_places=2, max_digits=5)
    wt= forms.DecimalField(decimal_places=2, max_digits=5)
    qsec= forms.DecimalField(decimal_places=2, max_digits=5)
    vs= forms.IntegerField()
    am= forms.IntegerField()
    gear= forms.IntegerField()
    carb= forms.IntegerField()

class DeleteForm(forms.Form):
    CarName= forms.CharField(max_length=20)
