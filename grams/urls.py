from django.urls import path

from .views import *

urlpatterns = [
    
    path('', Home, name='home'),
    path('course', CoursListView.as_view(), name='list'),
    path('course/<int:pk>', CoursDetailView.as_view(), name='detail'),
    
    path('student', EtudiantListView.as_view(), name='list'),
    path('student/<int:pk>', EtudiantDetailView.as_view(), name='detail'),
    
    path('teacher', EnseignantListView.as_view(), name='list'),
    path('teacher/<int:pk>', EnseignantDetailView.as_view(), name='detail'),

    path('exam', ExamListView.as_view(), name='list'),
    path('exam/<int:pk>', ExamDetailView.as_view(), name='detail'),

    path('classroom', SalleListView.as_view(), name='list'),
    path('classroom/<int:pk>', SalleDetailView.as_view(), name='detail'),

    path('event', EvenementListView.as_view(), name='list'),
    path('event/<int:pk>', EvenementDetailView.as_view(), name='detail'),

    path('user', UserListView.as_view(), name='list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='detail'),

    path('semestre', SemestreListView.as_view(), name='list'),
    path('semestre/<int:pk>', SemestreDetailView.as_view(), name='detail'),
]
