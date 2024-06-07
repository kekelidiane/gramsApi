from django.test import TestCase

from django.urls import reverse
from rest_framework import status

from ..models import Course
# Create your tests here.
                
class CourseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course = Course.objects.create(
            codeCourse = 'MTH225',
            name = 'Theorie des graphes',
            description = 'UE de maths etc etc ..........',
            schedule = '1- Introooooo',
        )
        
    def test_course_content(self):
        self.assertEqual(self.course.codeCourse, 'MTH225')
        self.assertEqual(self.course.name, 'Theorie des graphes')
        self.assertEqual(self.course.description, 'UE de maths etc etc ..........')
        self.assertEqual(self.course.schedule, '1- Introooooo')
        
    def test_course_listview(self):
        response = self.client.get(reverse('course'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Theorie')
        self.assertTemplateUsed(response, 'list.html')
        
    # def tearDown(self):
    #     # Supprimer l'instance après le test
    #     self.course.delete()    