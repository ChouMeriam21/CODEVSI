from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    id = models.BigAutoField(primary_key = True)
    nom = models.fields.CharField(max_length=100)
    prénom = models.fields.CharField(max_length=100)
    email = models.fields.EmailField(unique=True)
    mot_de_passe = models.fields.CharField(max_length = 20)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self): #Fonction qui sert retourne une chaîne de caractère pour identifier l'instance de la classe
        return self.nom + " " + self.prénom

class Statut(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.fields.CharField(max_length=100)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.nom

class Utilisateur_Statut(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_statut = models.ForeignKey(Statut, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)

    class Meta :
        unique_together = ('id_utilisateur', 'id_statut')
    
    def __str__(self):
        return self.commentaire


class Responsabilité(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    resp_pièce = models.BooleanField()
    resp_clé = models.BooleanField()
    resp_machine = models.BooleanField()
    resp_ressource_info = models.BooleanField()
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return str(self.id_utilisateur)

class Machine(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.commentaire

class Utilisateur_Machine(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)

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
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_ressource = models.ForeignKey(Ressource_Info, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)

    class Meta :
        unique_together = ('id_utilisateur', 'id_ressource')
    
    def __str__(self):
        return self.commentaire

class Rôle(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length = 100)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.nom

class Utilisateur_Rôle(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_rôle = models.ForeignKey(Rôle, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)

    class Meta :
        unique_together = ('id_utilisateur', 'id_rôle')
    
    def __str__(self):
        return self.commentaire

class Pièce(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_salle = models.CharField(max_length = 100)
    commentaire = models.fields.CharField(max_length = 150)

    def __str__(self):
        return self.nom_salle

class Utilisateur_Pièce(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_pièce = models.ForeignKey(Pièce, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)

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
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, primary_key = True)
    id_clef = models.ForeignKey(Clé, on_delete=models.CASCADE)
    date_début = models.DateField()
    date_fin = models.DateField()
    commentaire = models.fields.CharField(max_length = 150)

    class Meta :
        unique_together = ('id_utilisateur', 'id_clef')

    
    def __str__(self):
        return self.commentaire

class Pièce_Clé(models.Model):
    id_pièce = models.ForeignKey(Pièce, on_delete=models.CASCADE, primary_key = True)
    id_clé = models.ForeignKey(Clé, on_delete=models.CASCADE)
    commentaire = models.fields.CharField(max_length = 150)

    class Meta :
        unique_together = ('id_pièce', 'id_clé')

    def __str__(self):
        return self.commentaire