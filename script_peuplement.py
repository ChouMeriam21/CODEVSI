'''
Ce script sert à peupler la base de données avec des fichiers csv.
Les fichiers doivent être sous cette forme (par exemple pour les pièces): 

ID,nom_salle,commentaire
0,salle1,commentaire1
1,salle2,commentaire2
2,salle3,commentaire3
3,salle4,commentaire4
4,salle5,commentaire5

et doivent s'appeler respectivement : 
'pièces.csv' pour les pièces
'utilisateurs.csv' pour les utilisateurs
'machines.csv' pour les machines
'clés.csv' pour les clés
'ressources_info' pour les ressources informatiques*

Les fichiers csv doivent être dans le même répertoire que l'appli meeressources.

Si cette erreur s'affiche : django.core.exceptions.ImproperlyConfigured: Requested setting LOGGING_CONFIG, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
Lancer cette commande: export DJANGO_SETTINGS_MODULE=CODEVSI.settings

Selon quel type de donnée vous souhaiter peupler, il faut mettre en commentaire ou non les parties du code correspondantes. 
'''
import csv
import pandas as pd
import django
django.setup()
from meeressources.models import *

tmp_data_pièces = pd.read_csv('pièces.csv',sep=',') 

pièces = [
    Pièce(
        nom_salle = tmp_data_pièces.loc[row]['nom_salle'],
        commentaire = tmp_data_pièces.loc[row]['commentaire'],
    )
    for row in tmp_data_pièces['ID']
]
Pièce.objects.bulk_create(pièces)


# tmp_data_utilisateurs = pd.read_csv('utilisateurs.csv',sep=',')

# utilisateurs = [
#     Utilisateur(
#         nom = tmp_data_utilisateurs.loc[row]['nom'],
#         prénom = tmp_data_utilisateurs.loc[row]['prénom'],
#         email = tmp_data_utilisateurs.loc[row]['email'],
#         mot_de_passe = tmp_data_utilisateurs.loc[row]['mot_de_passe'], #Je ne sais pas si c'est vraiment judicieux de mettre les mots de passe de cette manière
#         commentaire = tmp_data_utilisateurs.loc[row]['commentaire'],
#     )
#     for row in tmp_data_utilisateurs['ID']
# ]
# Utilisateur.objects.bulk_create(utilisateurs)

# tmp_data_machines = pd.read_csv('machines.csv',sep=',')

# machines = [
#     Machine(
#         commentaire = tmp_data_machines.loc[row]['commentaire'],
#     )
#     for row in tmp_data_machines['ID']
# ]
# Machine.objects.bulk_create(machines)

# tmp_data_clés = pd.read_csv('clés.csv',sep=',')

# clés = [
#     Clé(
#         commentaire = tmp_data_clés.loc[row]['commentaire'],
#     )
#     for row in tmp_data_clés['ID']
# ]
# Clé.objects.bulk_create(clés)

# tmp_data_ressources_info = pd.read_csv('ressources_info.csv',sep=',')

# ressources_info = [
#     Ressource_Info(
#         commentaire = tmp_data_ressources_info.loc[row]['commentaire'],
#     )
#     for row in tmp_data_ressources_info['ID']
# ]
# Ressource_Info.objects.bulk_create(ressources_info)
