from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import *
from accounts.models import CustomUser

# Create your views here.

def Home(request):
    return render(request, 'index.html')

class SalleListView(ListView):
    model = Salle
    template_name = 'list.html'
    
class SalleDetailView(DetailView):
    model = Salle
    template_name = 'detail.html'
    context_object_name = 'classroom'

#--------------------------------------
class CoursListView(ListView):
    model = Cours
    template_name = 'list.html'
    
class CoursDetailView(DetailView):
    model = Cours
    template_name = 'detail.html'
    context_object_name = 'course'

#--------------------------------------    
class EtudiantListView(ListView):
    model = Etudiant
    template_name = 'list.html'
    
class EtudiantDetailView(DetailView):
    model = Etudiant
    template_name = 'detail.html'
    
#--------------------------------------
class EnseignantListView(ListView):
    model = list
    template_name = 'list.html'

class EnseignantDetailView(DetailView):
    model = Enseignant
    template_name = 'detail.html'
#--------------------------------------    
class ExamListView(ListView):
    model = Exam
    template_name = 'list.html'

class ExamDetailView(DetailView):
    model = Exam
    template_name = 'detail.html'
    
#--------------------------------------    
class EvenementListView(ListView):
    model = Evenement
    template_name = 'list.html'

class EvenementDetailView(DetailView):
    model = Evenement
    template_name = 'detail.html'
    context_object_name = 'event'
    
#--------------------------------------
class UserListView(ListView):
    model = CustomUser
    template_name = 'list.html'
    
class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'detail.html'
    context_object_name = 'user'
    
#--------------------------------------
class FiliereListView(ListView):
    model = Filiere
    template_name = 'list.html'
    
class FiliereDetailView(DetailView):
    model = Filiere
    template_name = 'detail.html'
    context_object_name = 'user'

#--------------------------------------
class DepartementListView(ListView):
    model = Departement
    template_name = 'list.html'
    
class DepartementDetailView(DetailView):
    model = Departement
    template_name = 'detail.html'

#--------------------------------------
class SemestreListView(ListView):
    model = Semestre
    template_name = 'list.html'
    
class SemestreDetailView(DetailView):
    model = Semestre
    template_name = 'detail.html'