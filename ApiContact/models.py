from django.db import models

class FormAssur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    situation = models.CharField(max_length=100)
    banque = models.CharField(max_length=100)
    accepter = models.BooleanField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class MutuelleCatalog(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    accepter = models.BooleanField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Contact(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    postal_code = models.CharField(max_length=10)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    data_usage = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"