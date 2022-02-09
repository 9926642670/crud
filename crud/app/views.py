from multiprocessing import context
from pickle import NONE
from django.shortcuts import render, HttpResponse, redirect
from .models import Persondetail

# Create your views here.
def show(request):
    tr = Persondetail.objects.all()
    return render(request, "show.html", {"tr":tr})

def update(request, id):
    tr = Persondetail.objects.get(pk=id) 
    if request.method == "POST":
        if request.FILES:
            img = request.FILES["image"]
        else:
            img = tr.__dict__['images']        

            
        name = request.POST["name"]
        age = request.POST["age"]
        mobno = request.POST["mobno"]
        gen = request.POST["gender"]
        obj = Persondetail.objects.get(pk = id)
        obj.name = name
        obj.age = age
        obj.mob_no = mobno
        obj.gender = gen
        obj.images = img
        obj.save()
        return redirect ("/show/")
    else:
        return render(request, "update.html", {"tr":tr})

def create(request):
    if request.method == "POST" and request.FILES:
        name = request.POST["name"]
        age = request.POST["age"]
        mobno = request.POST["mobno"]
        gen = request.POST["gender"]
        img = request.FILES["image"]
        obj = Persondetail(name = name, age = age, mob_no = mobno, gender = gen, images = img)
        obj.save()

    return render(request, "create.html")


def delete(request, id):
    obj =  Persondetail.objects.get(pk = id)  
    obj.delete()  
    return redirect("/show/")

