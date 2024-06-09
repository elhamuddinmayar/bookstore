from django.shortcuts import render
from .models import Bookstore
def index(request):
    return render(request,"index.html")

def bookstore(request):
    computer=Bookstore.objects.filter(collection_id="1")
    islamic=Bookstore.objects.filter(collection_id="2")
    fictional=Bookstore.objects.filter(collection_id="3")
    historical=Bookstore.objects.filter(collection_id="4")
    Litrary=Bookstore.objects.filter(collection_id="5")
    coding=Bookstore.objects.filter(collection_id="6")
    art=Bookstore.objects.filter(collection_id="7")
    medical=Bookstore.objects.filter(collection_id="8")
    science=Bookstore.objects.filter(collection_id="9")
    politics=Bookstore.objects.filter(collection_id="10") 
    
    return render(request,"bookstore.html",{"computer":computer,"islamic":islamic,"fictional":fictional,"historica":historical,"litrary":Litrary,"coding":coding,"art":art,"medical":medical,"science":science,"politics":politics})

def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

