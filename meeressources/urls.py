from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fiche/',views.page, name='page'),
    path('membresMEE/',views.PageMembres, name='membresMEE'),
    path('modifier/',views.Modifier, name='modifier'),
    path('inscription/',views.Inscription, name='inscription'),
]