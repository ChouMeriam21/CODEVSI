from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic 
from django.contrib.auth.models import User
from django.http import HttpRequest

# Create your views here.
def index(request):
    return render(request, 'registration/login.html')

def PageMembre(request):


    Username = request.user.username
    First_name = request.user.first_name
    Last_name = request.user.last_name
    Email = request.user.email

    context = {
        'Username' : Username,
        'First_name' : First_name,
        'Last_name' : Last_name,
        'Email' : Email,
    }

    return render(request, 'PageMembre.html', context = context)

def PageAdmin(request):


    Username = request.user.username
    First_name = request.user.first_name
    Last_name = request.user.last_name
    Email = request.user.email
    context = {
        'Username' : Username,
        'First_name' : First_name,
        'Last_name' : Last_name,
        'Email' : Email,
    }

    return render(request, 'PageAdmin.html', context = context)

def Inscription(request):
    return render(request, 'Inscription.html')


class RessourceInfoListView(generic.ListView):
    model = Ressource_Info

class MachineListView(generic.ListView):
    model = Machine

def choixPage(request):
    return render(request, 'choixPage.html')

