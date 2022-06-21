from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic 

# Create your views here.
def index(request):
    return render(request, 'PageAccueil.html')
def PageAdmin(request):

    Id = Utilisateur.id
    Nom = Utilisateur.nom

    context = {
        'Id' : Id,
        'Nom' : Nom,
    }

    return render(request, 'PageAdmin.html', context = context)
def membresMEE(request):

    NombreDeMembres = Utilisateur.objects.all().count()
    NombreAdmin = Utilisateur.objects.filter(rôle = 'a').count()
    context = {
        'NombreDeMembres': NombreDeMembres,
        'NombreAdmin': NombreAdmin,
    }
    return render(request, 'membresMEE.html', context = context)

def Modifier(request):
    return render(request, 'Modifier.html')
def Inscription(request):
    return render(request, 'Inscription.html')


class RessourceInfoListView(generic.ListView):
    model = Ressource_Info

class MachineListView(generic.ListView):
    model = Machine