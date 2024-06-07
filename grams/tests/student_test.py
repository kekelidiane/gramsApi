from django.test import TestCase

from django.urls import reverse
from rest_framework import status

from ..models import Student
# Create your tests here.
        
        
class StudentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = Student.objects.create(
            numCard = '541289',
            name = 'ADAKO Kodjo Georges',
            birthday = '2005-2-9',
            semester = 3,
            email = 'kodjo@gmail.com',
            address = 'Adjololo',
            contact = 90000001
        )
        
    def test_student_content(self):
        self.assertEqual(self.student.numCard, '541289')
        self.assertEqual(self.student.name, 'ADAKO Kodjo Georges')
        self.assertEqual(self.student.birthday, '2005-2-9')
        self.assertEqual(self.student.semester, 3 )
        self.assertEqual(self.student.email, 'kodjo@gmail.com')
        self.assertEqual(self.student.address, 'Adjololo')
        self.assertEqual(self.student.contact, 90000001)
        
    def test_student_listview(self):
        response = self.client.get(reverse('student'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Kodjo')
        self.assertTemplateUsed(response, 'list.html')