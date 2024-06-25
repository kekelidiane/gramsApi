from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Salle)
admin.site.register(Etudiant)
admin.site.register(Cours)
admin.site.register(Exam)
admin.site.register(Enseignant)
admin.site.register(Reservation)
admin.site.register(Filiere)
admin.site.register(Departement)
admin.site.register(Semestre)

