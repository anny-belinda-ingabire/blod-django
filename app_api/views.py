from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def contact(request):
    contact = Contact.objects.all()
    print(contact)
    return render(request, "index.html",{"contacts":contact})

def utilisateur(request):
    msg ="toute les utilisateur"
    return HttpResponse(msg)

