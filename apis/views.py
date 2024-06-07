from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from grams.models import *
from accounts.models import CustomUser
from grams.serializers import *

# Create your apis views here.

#afficher la liste
class SalleAPIView(generics.ListCreateAPIView):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer    
    
class SalleDetail(generics.RetrieveAPIView): #afficher les details    
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    #lookup_field = 'id'
    permission_classes = (permissions.IsAdminUser,)
    
class CreateSalle(generics.CreateAPIView): #creer une nouvelle instance
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateSalle(generics.RetrieveUpdateAPIView): #mettre à jour une instance
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteSalle(generics.DestroyAPIView): #supprimer une instance
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    permission_classes = (permissions.IsAdminUser,)
    
#------------------------------------------------------------------------------------

class CoursAPIView(generics.ListCreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    
class CoursDetail(generics.RetrieveAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class CreateCours(generics.CreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateCours(generics.RetrieveUpdateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteCours(generics.DestroyAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    permission_classes = (permissions.IsAdminUser,)
        
#------------------------------------------------------------------------------------

class EtudiantAPIView(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    
class EtudiantDetail(generics.RetrieveAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class CreateEtudiant(generics.CreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateEtudiant(generics.RetrieveUpdateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteEtudiant(generics.DestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = (permissions.IsAdminUser,)
    
#------------------------------------------------------------------------------------
    
class EnseignantAPIView(generics.ListCreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    
class EnseignantDetail(generics.RetrieveAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    permission_classes = (permissions.IsAdminUser,)
        
class CreateEnseignant(generics.CreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateEnseignant(generics.RetrieveUpdateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteEnseignant(generics.DestroyAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    permission_classes = (permissions.IsAdminUser,)
    
#------------------------------------------------------------------------------------

class ExamAPIView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    
class ExamDetail(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAdminUser,)

class CreateExam(generics.CreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateExam(generics.RetrieveUpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteExam(generics.DestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAdminUser,)
        
#------------------------------------------------------------------------------------
    
class EvenementAPIView(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
        
class CreateEvenement(generics.CreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class EvenementDetail(generics.RetrieveAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateEvenement(generics.RetrieveUpdateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteEvenement(generics.DestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    permission_classes = (permissions.IsAdminUser,)
        
#------------------------------------------------------------------------------------

class UserAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CreateUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteUser(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    
#------------------------------------------------------------------------------------

class DepartementAPIView(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    
class DepartementDetail(generics.RetrieveAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class CreateDepartement(generics.CreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateDepartement(generics.RetrieveUpdateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteDepartement(generics.DestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = (permissions.IsAdminUser,)
        
#------------------------------------------------------------------------------------

class FiliereAPIView(generics.ListCreateAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    
class FiliereDetail(generics.RetrieveAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class CreateFiliere(generics.CreateAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateFiliere(generics.RetrieveUpdateAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteFiliere(generics.DestroyAPIView):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    permission_classes = (permissions.IsAdminUser,)
        
#------------------------------------------------------------------------------------

class SemestreAPIView(generics.ListCreateAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer
    
class SemestreDetail(generics.RetrieveAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class CreateSemestre(generics.CreateAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class UpdateSemestre(generics.RetrieveUpdateAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class DeleteSemestre(generics.DestroyAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer
    permission_classes = (permissions.IsAdminUser,)
        
#------------------------------------------------------------------------------------