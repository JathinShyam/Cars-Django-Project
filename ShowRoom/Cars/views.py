from django.shortcuts import render
from .models import Car
import csv
from .forms import CarForm, DeleteForm
from .email import *

# Create your views here.
from django.http import HttpResponse

def index(request):

    return render(request, 'Cars/index.html')

'''def update(request):
    with open('cars.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = Car(CarName=row[""], mpg=row['mpg'], cyl=row["cyl"], disp=row['disp'], hp=row["hp"], drat=row['drat'], wt=row["wt"], qsec=row['qsec'], vs=row["vs"], am=row['am'], gear=row["gear"], carb=row['carb'], )
            data.save()
            
    return HttpResponse('Data Uploaded!!')
'''

def enter(request):
    if request.method=='POST':
        form = CarForm(request.POST)
        if form.is_valid():

            x=Car()

            x.CarName= form.cleaned_data["CarName"]
            x.mpg= form.cleaned_data['mpg']
            x.cyl= form.cleaned_data['cyl']
            x.disp= form.cleaned_data['disp']
            x.hp= form.cleaned_data['hp']
            x.drat= form.cleaned_data['drat']
            x.wt= form.cleaned_data['wt']
            x.qsec= form.cleaned_data['qsec']
            x.vs= form.cleaned_data['vs']
            x.am= form.cleaned_data['am']
            x.gear= form.cleaned_data['gear']
            x.carb= form.cleaned_data['carb']

            q=Car.objects.all()
            for i in q:
                if i.CarName == x.CarName:
                    i.mpg= x.mpg
                    i.cyl= x.cyl
                    i.disp=x.disp
                    i.hp=x.hp
                    i.drat=x.drat
                    i.wt= x.wt
                    i.qsec=x.qsec
                    i.vs= x.vs
                    i.am= x.am
                    i.gear= x.gear
                    i.carb= x.carb
                    i.save()
                    return HttpResponse("Updated Successfully!")
                
            x.save()       
            return HttpResponse(f"Entered Successfully!")
    else:
        form= CarForm
    
    return render(request, 'Cars/update.html',{'form':form})

def display(request):
    q=Car.objects.all()
    return render(request,'Cars/display.html',{'q':q})


def importData(request):
    rows = []
    fields= []
    cars={}
    q=Car.objects.all()
    for i in q:
        cars[i.CarName]=1

    with open('cars.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            x=Car()

            x.CarName= row[0]
            x.mpg= row[1]
            x.cyl= row[2]
            x.disp= row[3]
            x.hp= row[4]
            x.drat= row[5]
            x.wt= row[6]
            x.qsec= row[7]
            x.vs= row[8]
            x.am= row[9]
            x.gear= row[10]
            x.carb= row[11]
            rows.append(row)
            if x.CarName not in cars:
                cars[x.CarName] =1
                x.save()
        return HttpResponse('Imported Successfully!')

def updateFile(request):
    fields = ["CarName",'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
    rows = []
    with open('carsnew.csv', 'w') as csvfile:
        csvwriter=csv.writer(csvfile)
        q=Car.objects.all()
        for i in q:
            l=list()
            l.append(i.CarName)
            l.append(i.mpg)
            l.append(i.cyl)
            l.append(i.disp)
            l.append(i.hp)
            l.append(i.drat)
            l.append(i.wt)
            l.append(i.qsec)
            l.append(i.vs)
            l.append(i.am)
            l.append(i.gear)
            l.append(i.carb)

            rows.append(l)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
        return HttpResponse("New File Updated!")


def delete(request):
    if request.method=='POST':
        form = DeleteForm(request.POST)
        if form.is_valid():

            x=Car()
            x.CarName= form.cleaned_data["CarName"]
            q=Car.objects.all()
            for i in q:
                if i.CarName == x.CarName:
                    i.delete()
                    return HttpResponse("Deleted Successfully!")
                       
            return HttpResponse(f"No Entry Available!")
    else:
        form= DeleteForm
    
    return render(request, 'Cars/delete.html',{'form':form})

def mailing(request):
    q=Car.objects.all()
    str1= ""
    for i in q:
        str1=str1+(f"Car Name: {i.CarName}, mpg: {i.mpg}, cyl: {i.cyl}, disp: {i.disp}, hp: {i.hp}, drat: {i.drat}, wt: {i.wt}, qsec: {i.qsec}, vs: {i.vs}, am: {i.am}, gear: {i.gear}, carb: {i.carb}\n")

    sendemail(str1)
    return HttpResponse("Email Sent!")