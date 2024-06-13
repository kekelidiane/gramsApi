from rest_framework import serializers

from .models import *
from accounts.models import CustomUser

#--------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'email', 'address', 'phone']

#--------------------------------------------------

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = '__all__'

#--------------------------------------------------
  
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Etudiant
        fields = '__all__'

#--------------------------------------------------

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'

#--------------------------------------------------

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = '__all__'

#--------------------------------------------------

class CoursSerializer(serializers.ModelSerializer):
    option = serializers.SerializerMethodField()

    class Meta:
        model = Cours
        fields = '__all__'
        
    def get_option(self, obj):
        return [filiere.nom for filiere in obj.option.all()]
#--------------------------------------------------

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

#--------------------------------------------------

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'

#--------------------------------------------------

class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = '__all__'

#--------------------------------------------------

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

