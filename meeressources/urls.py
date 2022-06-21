from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('choixPage/', views.choixPage, name = 'choixPage'),
        path('PageAdmin/',views.PageAdmin, name='PageAdmin'),
        path('PageMembre/',views.PageMembre, name = 'PageMembre'),
        path('inscription/',views.Inscription, name='inscription'),
        path('ressourcesInfo/', views.RessourceInfoListView.as_view(), name='ressourcesInfo'),
        path('machines/', views.MachineListView.as_view(), name='machines'),

]

