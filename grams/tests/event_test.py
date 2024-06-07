from django.test import TestCase

from django.urls import reverse
from rest_framework import status

from ..models import Event
# Create your tests here.  

class EventTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.create(
            codeEvent = 'EV001',
            name = 'Exam',
            date = '2024-2-29',
            hour = '10:00:00',
            duration = 2,
        )
        
    def test_classroom_content(self):
        self.assertEqual(self.event.codeEvent, 'EV001')
        self.assertEqual(self.event.name, 'Exam')
        self.assertEqual(self.event.date, '2024-2-29')
        self.assertEqual(self.event.hour, '10:00:00')
        self.assertEqual(self.event.duration, 2)
        
    def test_classroom_listview(self):
        response = self.client.get(reverse('event'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Exam')
        self.assertTemplateUsed(response, 'list.html')
