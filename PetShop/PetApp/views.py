from django.shortcuts import render
from .models import Pet

# Create your views here.
def get_all(request, kind=""):  
    kind = kind.capitalize()
    if kind in ["Dog", "Cat"]:  
        pets = Pet.objects.filter(type=kind)    
    else:
        pets = Pet.objects.all()
    count = pets.count()
    return render(request, "PetApp/home.html", 
                  {"pets":pets, "count": count})

