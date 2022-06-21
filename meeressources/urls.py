from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('PageAdmin/',views.PageAdmin, name='PageAdmin'),
        path('membresMEE/',views.membresMEE, name='membresMEE'),
        path('modifier/',views.Modifier, name='modifier'),
        path('inscription/',views.Inscription, name='inscription'),
        path('ressourcesInfo/', views.RessourceInfoListView.as_view(), name='ressourcesInfo'),
        path('machines/', views.MachineListView.as_view(), name='machines'),
]

