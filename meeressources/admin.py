from django.contrib import admin

# Register your models here.

from meeressources.models import *

admin.site.register(Utilisateur)
admin.site.register(Statut)
admin.site.register(Utilisateur_Statut)
admin.site.register(Responsabilité)
admin.site.register(Machine)
admin.site.register(Utilisateur_Machine)
admin.site.register(Ressource_Info)
admin.site.register(Utilisateur_Ressource_Info)
admin.site.register(Rôle)
admin.site.register(Utilisateur_Rôle)
admin.site.register(Pièce)
admin.site.register(Utilisateur_Pièce)
admin.site.register(Clé)
admin.site.register(Utilisateur_Clé)
admin.site.register(Pièce_Clé)
