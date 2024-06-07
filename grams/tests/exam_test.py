from django.test import TestCase

from django.urls import reverse
from rest_framework import status

from ..models import Exam, Course, Teacher
# Create your tests here.


        

class ExamTest(TestCase):
    @classmethod
    def setUpClass(cls):
        
        #Course's instance       
        cls.course = Course.objects.create(
            codeCourse = 'MTH225',
            name = 'Theorie des graphes',
            description = 'UE de maths etc etc ..........',
            schedule = '1- Introooooo',
        )
        
        cls.exam = Exam.objects.create(
            codeExam = 'EX001',
            name = cls.course,
            date = '2024-2-29',
            hour = '13:00:00',
            duration = 2,
        )
        
    def test_exam_content(self):
        self.assertEqual(self.exam.codeExam, 'EX001')
        self.assertEqual(self.exam.name.name, self.course.name)
        self.assertEqual(self.exam.date, '2024-2-29')
        self.assertEqual(self.exam.hour, '13:00:00')
        self.assertEqual(self.exam.duration, 2)
        
    def test_exam_listview(self):
        response = self.client.get(reverse('exam'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '2024')
        self.assertTemplateUsed(response, 'list.html')