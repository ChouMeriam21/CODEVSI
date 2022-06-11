from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'PageAccueil.html')
def page(request):
    return render(request, 'page.html')
def PageMembres(request):
    return render(request, 'PageMembres.html')
def Modifier(request):
    return render(request, 'Modifier.html')
def Inscription(request):
    return render(request, 'Inscription.html')
