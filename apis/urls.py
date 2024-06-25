from django.urls import path

from .views import *

urlpatterns = [
#--------------------------------urls des salles----------------------------------

    path('salle', SalleAPIView.as_view(), name='list'),  #affiche le liste
    path('salle/<int:pk>', SalleDetail.as_view(), name='classroom_detail'),   #affiche les details des instances 
    path('salle/add', CreateSalle.as_view(), name='create_classroom'), #create
    path('salle/<int:pk>/update', UpdateSalle.as_view(), name='update_classroom'), #update
    path('salle/<int:pk>/del', DeleteSalle.as_view(), name='delete_classroom'), #delete
    
#--------------------------------urls des cours----------------------------------

    path('cours', CoursAPIView.as_view(), name='list'),
    path('cours/<int:pk>', CoursDetail.as_view(), name='course_detail'),  
    path('cours/add', CreateCours.as_view(), name='create_course'),
    path('cours/<int:pk>/update', UpdateCours.as_view(), name='update_course'),
    path('cours/<int:pk>/del', DeleteCours.as_view(), name='delete_course'),  

#--------------------------------urls des etudiants----------------------------------

    path('etudiant', EtudiantAPIView.as_view(), name='list'),
    path('etudiant/<int:pk>', EtudiantDetail.as_view(), name='student_detail'),
    path('etudiant/add', CreateEtudiant.as_view(), name='create_student'),
    path('etudiant/<int:pk>/update', UpdateEtudiant.as_view(), name='update_student'),
    path('etudiant/<int:pk>/del', DeleteEtudiant.as_view(), name='delete_student'),

#--------------------------------urls des enseignants----------------------------------

    path('enseignant', EnseignantAPIView.as_view(), name='teacher'),
    path('enseignant/<int:pk>', EnseignantDetail.as_view(), name='teacher_detail'),
    path('enseignant/add', CreateEnseignant.as_view(), name='create_teacher'),
    path('enseignant/<int:pk>/update', UpdateEnseignant.as_view(), name='update_teacher'),
    path('enseignant/<int:pk>/del', DeleteEnseignant.as_view(), name='delete_teacher'),

#--------------------------------urls des examens----------------------------------

    path('exam', ExamAPIView.as_view(), name='list'),
    path('exam/<int:pk>', ExamDetail.as_view(), name='exam_detail'),
    path('exam/add', CreateExam.as_view(), name='create_exam'),
    path('exam/<int:pk>/update', UpdateExam.as_view(), name='update_exam'),
    path('exam/<int:pk>/del', DeleteExam.as_view(), name='delete_exam'),

#--------------------------------urls des reservations----------------------------------

    path('reservation', ReservationAPIView.as_view(), name='list'),
    path('event/<int:pk>', ReservationDetail.as_view(), name='event_detail'),
    path('event/add', CreateReservation.as_view(), name='create_event'),
    path('event/<int:pk>/update', UpdateReservation.as_view(), name='update_event'),
    path('event/<int:pk>/del', DeleteReservation.as_view(), name='delete_event'),

#--------------------------------urls des semestres----------------------------------

    path('semestre', SemestreAPIView.as_view(), name='list'),
    path('semestre/<int:pk>', SemestreDetail.as_view(), name='sem_detail'),
    path('semestre/add', CreateSemestre.as_view(), name='create_sem'),
    path('semestre/<int:pk>/update', UpdateSemestre.as_view(), name='update_sem'),
    path('semestre/<int:pk>/del', DeleteSemestre.as_view(), name='delete_sem'),

#--------------------------------urls des departements----------------------------------

    path('departement', DepartementAPIView.as_view(), name='list'),
    path('departement/<int:pk>', DepartementDetail.as_view(), name='depart_detail'),
    path('departement/add', CreateDepartement.as_view(), name='create_depart'),
    path('departement/<int:pk>/update', UpdateDepartement.as_view(), name='update_depart'),
    path('departement/<int:pk>/del', DeleteDepartement.as_view(), name='delete_depart'),

#--------------------------------urls des filieres----------------------------------

    path('filiere', FiliereAPIView.as_view(), name='list'),
    path('filiere/<int:pk>', FiliereDetail.as_view(), name='event_fil'),
    path('filiere/add', CreateFiliere.as_view(), name='create_fil'),
    path('filiere/<int:pk>/update', UpdateFiliere.as_view(), name='update_fil'),
    path('filiere/<int:pk>/del', DeleteFiliere.as_view(), name='delete_fil'),

#--------------------------------urls des uers----------------------------------

    path('user', UserAPIView.as_view(), name='list'),    
    path('user/add', CreateUser.as_view(), name='create_user'),
    path('user/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('user/<int:pk>/update', UpdateUser.as_view(), name='update_user'),
    path('user/<int:pk>/del', DeleteUser.as_view(), name='delete_user'),

]