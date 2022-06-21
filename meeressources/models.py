from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    id = models.BigAutoField(primary_key = True)                   # Auto-incrémentation de la clé primaire
    nom = models.fields.CharField(max_length=100)
    prénom = models.fields.CharField(max_length=100)
    email = models.fields.EmailField(unique=True)
    ROLES = (                                            #On fixe les différents rôles pour pouvoir filtré les utilisateurs selon leur rôle.
        ('a', 'Administrateur'),
        ('u', 'Utilisateur_simple'),
        ('d', 'Administrateur_délégué'),
    )
    rôle = models.CharField(
        max_length=1,
        choices=ROLES,
        blank=True,
        default='u',
    )
    mot_de_passe = models.fields.CharField(max_length = 20)         # La valeur max est arbitraire
    commentaire = models.fields.CharField(max_length = 150)         

    def __str__(self): #Fonction qui retourne une chaîne de caractère pour identifier l'instance de la classe
        return self.nom + " " + self.prénom

class Statut(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.fields.CharField(max_length=100)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.nom

class Utilisateur_Statut(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_statut = models.ForeignKey(Statut, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)

    class Meta :
        unique_together = ('id_utilisateur', 'id_statut')       # Pour gérer les clefs primaires à plusieurs attributs
    
    def __str__(self):
        return self.commentaire


class Machine(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.commentaire

class Utilisateur_Machine(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)
    responsable = models.BooleanField(default = False)

    class Meta :
        unique_together = ('id_utilisateur', 'id_machine')
    
    def __str__(self):
        return self.commentaire

class Ressource_Info(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.commentaire

class Utilisateur_Ressource_Info(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_ressource = models.ForeignKey(Ressource_Info, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)
    responsable = models.BooleanField(default = False)

    class Meta :
        unique_together = ('id_utilisateur', 'id_ressource')
    
    def __str__(self):
        return self.commentaire

class Pièce(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_salle = models.CharField(max_length = 100)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.nom_salle

class Utilisateur_Pièce(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_pièce = models.ForeignKey(Pièce, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)
    responsable = models.BooleanField(default = False)

    class Meta :
        unique_together = ('id_utilisateur', 'id_pièce')
    
    def __str__(self):
        return self.commentaire


class Clé(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.commentaire

class Utilisateur_Clé(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_clef = models.ForeignKey(Clé, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)
    responsable = models.BooleanField(default = False)

    class Meta :
        unique_together = ('id_utilisateur', 'id_clef')

    
    def __str__(self):
        return self.commentaire

class Pièce_Clé(models.Model):
    id_pièce = models.OneToOneField(Pièce, on_delete=models.CASCADE, primary_key = True)
    id_clé = models.ForeignKey(Clé, on_delete=models.CASCADE)
    commentaire = models.fields.CharField(max_length = 150)

    class Meta :
        unique_together = ('id_pièce', 'id_clé')

    def __str__(self):
        return self.commentaire