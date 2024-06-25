from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class TypeUser(models.TextChoices):
    ETU = 'ETU', _('Etudiant à l\'EPL')
    ENS = 'ENS', _('Enseignant à l\'EPL')
    INV = 'INV', _('Invite (Etudiant ou Enseignant d\'autres facultés, écoles)')

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Veuillez spécifier l\'adresse mail')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Un superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Un superutilisateur doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True) 
    date_naissance = models.DateField()
    contact = models.CharField(max_length=150)
    adresse = models.CharField(max_length=100)
    type_compte = models.CharField(
        max_length=3,
        choices=TypeUser.choices,
        default=TypeUser.ETU,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'password', 'date_naissance', 'contact']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
