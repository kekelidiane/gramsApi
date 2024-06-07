from django.db import models

# Create your models here.

        
class Semestre(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    codeSem = models.CharField(max_length=10)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    
class Dispo(models.TextChoices):
    Oui = 'oui'
    Non = 'non'

class Etat(models.TextChoices):
    Libre = 'lib'
    Occupée = 'occ'
    Reservée = 'res'

class Salle(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    codeSalle = models.CharField(max_length=10)
    nom = models.CharField(max_length=50)
    capacite = models.IntegerField()
    localisation = models.CharField(max_length=100)
    disponibilite = models.CharField(
        # max_length=3,
        choices=Dispo,
        default=Dispo.Oui
    )
    etat = models.CharField(
        choices=Etat,
        default=Etat.Libre
    )
    
    def __str__(self):
        return self.nom
    
class Etudiant(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    numCarte = models.IntegerField()
    nom = models.CharField(max_length=100)
    mail = models.EmailField(max_length=25)
    date_naissance = models.DateField()
    contact = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    semestre  = models.ForeignKey(Semestre, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.nom
    
class Enseignant(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    nom = models.CharField(max_length=100)
    mail = models.EmailField(max_length=25)
    contact = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    disponibilite = models.CharField(
        max_length=3,
        choices=Dispo,
        default=Dispo.Oui
    )
    
    def __str__(self):
        return self.nom

class Departement(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    codeDep = models.CharField(max_length=10)
    nom = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nom
    
class Parcours(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    codeDep = models.CharField(max_length=10)
    nom = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nom

class Filiere(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    codeFiliere = models.CharField(max_length=10)
    nom = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
    
class Cours(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    codeUe = models.CharField(max_length=10)
    intitule = models.CharField(max_length=50)
    prerequis = models.CharField(max_length=150)
    semestre_evolution = models.ForeignKey(Semestre, related_name="semestre_evolution", on_delete=models.CASCADE)
    semestre_etude = models.ForeignKey(Semestre, related_name="semestre_etude" ,on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    option = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.intitule
 
class Exam(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    codeExam = models.CharField(max_length=10)
    filiere = models.ManyToManyField(Filiere)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)    
    date = models.DateField()
    debut = models.DateTimeField((""), auto_now=True)
    fin = models.DateTimeField((""), auto_now=True)

    
    def __str__(self):
        return self.codeExam    
    
class Evenement(models.Model):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    nom = models.CharField(max_length=100)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    description = models.TextField(max_length=25)
    date = models.DateField()
    duree = models.IntegerField()
    debut = models.DateTimeField((""), auto_now=True)
    fin = models.DateTimeField((""), auto_now=True)
    
    def __str__(self):
        return self.nom


# class User(models.Model):
#     codeUser = models.CharField(max_length=10)
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=25)
    
#     def __str__(self):
#         return self.name