from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import *
from accounts.models import CustomUser

#--------------------------------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('nom', 'email', 'password', 'contact', 'adresse')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            nom=validated_data['nom'],
            email=validated_data['email'],
            password=validated_data['password'],
            contact=validated_data['contact'],
            adresse=validated_data['adresse'],
        )
        return user

#--------------------------------------------------

class LoginSerializer(serializers.Serializer):
    nom = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Utilisateur ou Mot de passe incorrect!")

#--------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'nom', 'mail', 'adresse', 'contact']

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
    parcours = serializers.SerializerMethodField()
    departement = serializers.SerializerMethodField()

    class Meta:
        model = Filiere
        fields = '__all__'
    
    def get_parcours(self, obj):
        return obj.parcours.nom

    def get_departement(self, obj):
        return obj.departement.nom

#--------------------------------------------------

class CoursSerializer(serializers.ModelSerializer):
    option = serializers.SerializerMethodField() # et le def permettent d'afficher les noms des attributs et non leur id dans la recup

    class Meta:
        model = Cours
        fields = '__all__'
        
    def get_option(self, obj):
        return obj.option.nom
#--------------------------------------------------

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

#--------------------------------------------------

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
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


