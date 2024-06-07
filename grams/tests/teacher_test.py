from django.test import TestCase

from django.urls import reverse
from rest_framework import status

from ..models import Teacher
from accounts.models import CustomUser
# Create your tests here.
        
    
class TestTeacher(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.teacher = Teacher.objects.create(
            codeTeacher = 'DrTEPE',
            name = 'TEPE',
            email = 'tepe@gmail.com',
            contact = 99885522,
            address = 'Adjidogome',
            availability = 'no'
        )
        
        cls.user = CustomUser.objects.create(
            username = 'teach',
            name = 'TEACHER',
            email = 't@gmail.com',
            address = 'Agoe',
            # phone = '',
            is_admin = 'yes'
        )
        
        # cls.client.login(username='teach', password='123456789')
        
    def test_teacher_content(self):
        self.assertEqual(self.teacher.codeTeacher, 'DrTEPE')
        self.assertEqual(self.teacher.name, 'TEPE')
        self.assertEqual(self.teacher.email, 'tepe@gmail.com')
        self.assertEqual(self.teacher.contact, 99885522)
        self.assertEqual(self.teacher.address, 'Adjidogome')
        self.assertEqual(self.teacher.availability, 'no')
        
    def test_teacher_listview(self):
        response = self.client.get(reverse('teacher'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'tepe')
        self.assertTemplateUsed(response, 'list.html')
        
    # def test_teacher_detailview(self): 
    #     response = self.client.get(
    #         reverse("teacher_detail", kwargs={"pk": self.teacher.codeTeacher}),
    #         format="json"
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Teacher.objects.count(), 1)
    #     self.assertContains(response, "Tepe")
