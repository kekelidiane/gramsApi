from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TypeUser(models.TextChoices):
    # admin = 'Administrateur',
    etu = 'Etudiant à l\'EPL',
    ens = 'Enseignant à l\'EPL',
    inv = 'Invite (Etudiant ou Enseignant d\'autres facultés, écoles)'
    
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    nom = models.CharField(max_length=100)
    mail = models.EmailField(max_length=50)
    type_compte = models.CharField(
        choices=TypeUser,
        default=TypeUser.etu
    )
    contact = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100, blank=True)
    