from django.contrib import admin

# Register your models here.

from meeressources.models import *

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prénom', 'email', 'commentaire')

admin.site.register(Utilisateur, UtilisateurAdmin)

class StatutAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'commentaire')

admin.site.register(Statut, StatutAdmin)

class Utilisateur_StatutAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'id_statut', 'date_début', 'date_fin', 'commentaire')

admin.site.register(Utilisateur_Statut, Utilisateur_StatutAdmin)

class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentaire')

admin.site.register(Machine, MachineAdmin)

class Utilisateur_MachineAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'id_machine', 'date_début', 'date_fin', 'commentaire', 'responsable')

admin.site.register(Utilisateur_Machine, Utilisateur_MachineAdmin)

class Ressource_InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentaire')

admin.site.register(Ressource_Info, Ressource_InfoAdmin)

class Utilisateur_Ressource_InfoAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'id_ressource', 'date_début', 'date_fin', 'commentaire', 'responsable')

admin.site.register(Utilisateur_Ressource_Info, Utilisateur_Ressource_InfoAdmin)

class RôleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'commentaire')

admin.site.register(Rôle, RôleAdmin)

class Utilisateur_RôleAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'id_rôle', 'date_début', 'date_fin', 'commentaire')

admin.site.register(Utilisateur_Rôle, Utilisateur_RôleAdmin)

class PièceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_salle', 'commentaire')

admin.site.register(Pièce, PièceAdmin)

class Utilisateur_PièceAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'id_pièce', 'date_début', 'date_fin', 'commentaire','responsable')

admin.site.register(Utilisateur_Pièce, Utilisateur_PièceAdmin)

class CléAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentaire')

admin.site.register(Clé, CléAdmin)

class Utilisateur_CléAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'id_clef', 'date_début', 'date_fin', 'commentaire', 'responsable')

admin.site.register(Utilisateur_Clé, Utilisateur_CléAdmin)

class Pièce_CléAdmin(admin.ModelAdmin):
    list_display = ('id_pièce', 'id_clé', 'commentaire')

admin.site.register(Pièce_Clé, Pièce_CléAdmin)



