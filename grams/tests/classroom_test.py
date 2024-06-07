from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone

from django.urls import reverse
from rest_framework import status

from ..models import Classroom
from accounts.models import CustomUser

# Create your tests here.
class ClassroomTest(TestCase):
    def test_create_classroom(self):
        # Create the post with the attributes
        classroom = Classroom(
            codeClass = 'AA',
            name = 'Amphi A',
            capacity = 100,
            location = 'EPL',
            availability = 'yes', 
            etat = 'Libre'
        )
        # Save it
        classroom.save()

        # Check we can find it
        all_classroom = Classroom.objects.all()
        self.assertEquals(len(all_classroom), 1)
        only_classroom = all_classroom[0]
        self.assertEquals(only_classroom, classroom)

        # Check attributes
        self.assertEqual(only_classroom.codeClass, 'AA')
        self.assertEqual(only_classroom.name, 'Amphi A')
        self.assertEqual(only_classroom.capacity, 100)
        self.assertEqual(only_classroom.location, 'EPL')
        self.assertEqual(only_classroom.availability, 'yes')
        self.assertEqual(only_classroom.etat, 'Libre')

class AdminTest(LiveServerTestCase):
    fixtures = ['user.json']

    def setUp(self):
        # Create client
        self.client = Client()

    def test_login(self):
        # Get login page
        response = self.client.get('http://127.0.0.1:8000/apis/user')

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)

        # Log the user in
        self.client.login(username='test', password="password")

        # Check response code
        response = self.client.get('http://127.0.0.1:8000/apis/user')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

    def test_logout(self):
        # Log in
        self.client.login(username='test', password="password")

        # Check the response code
        response = self.client.get('http://127.0.0.1:8000/apis/user')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('http://127.0.0.1:8000/apis/user')
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)

    def test_create_classroom(self):
        # Log in
        self.client.login(username='test', password="password")

        # Check response code
        response = self.client.get('http://127.0.0.1:8000/apis/classroom/add')
        self.assertEquals(response.status_code, 200)

        # Create the new post
        response = self.client.post('http://127.0.0.1:8000/apis/classroom/add', {
            'title': 'My first post',
            'text': 'This is my first post',
            'pub_date_0': '2013-12-28',
            'pub_date_1': '22:00:04'
        },
        follow=True
        )
        self.assertEquals(response.status_code, 200)

        # Check added successfully
        self.assertTrue('added successfully' in response.content)

        # Check new post now in database
        all_classroom = Classroom.objects.all()
        self.assertEquals(len(all_classroom), 1)

    def test_edit_classroom(self):
        # Create the post
        classroom = Classroom(
            codeClass = 'AA',
            name = 'Amphi A',
            capacity = 100,
            location = 'EPL',
            availability = 'yes', 
            etat = 'Libre'
        )
        # Save it
        classroom.save()

        # Log in
        self.client.login(username='test', password="password")

        # Edit the post
        response = self.client.post('http://127.0.0.1:8000/apis/classroom/5', {
            'codeClass' : 'AA',
            'name' : 'Amphi A',
            'capacity' : '100',
            'location' :'EPL',
            'availability' : 'yes', 
            'etat' : 'Libre'
        },
            follow=True
        )
        self.assertEquals(response.status_code, 200)

        # Check changed successfully
        self.assertTrue('changed successfully' in response.content)

        # Check post amended
        all_classroom = Classroom.objects.all()
        self.assertEquals(len(all_classroom), 1)
        only_classroom = all_classroom[0]
        self.assertEquals(only_classroom, classroom)
        
        self.assertEqual(only_classroom.codeClass, 'AA')
        self.assertEqual(only_classroom.name, 'Amphi A')
        self.assertEqual(only_classroom.capacity, 100)
        self.assertEqual(only_classroom.location, 'EPL')
        self.assertEqual(only_classroom.availability, 'yes')
        self.assertEqual(only_classroom.etat, 'Libre')

    def test_delete_classroom(self):
        # Create the post
        classroom = Classroom(
            codeClass = 'AA',
            name = 'Amphi A',
            capacity = 100,
            location = 'EPL',
            availability = 'yes', 
            etat = 'Libre'
        )
        # Save it
        classroom.save()

        # Check new post saved
        all_classroom = Classroom.objects.all()
        self.assertEquals(len(all_classroom), 1)

        # Log in
        self.client.login(username='test', password="password")

        # Delete the post
        response = self.client.post('http://127.0.0.1:8000/apis/classroom/5/del', {
            'classroom': 'yes'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue('deleted successfully' in response.content)

        # Check post amended
        all_classroom = Classroom.objects.all()
        self.assertEquals(len(all_classroom), 0)

class ClassroomViewTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        # Create the post
        classroom = Classroom(
            codeClass = 'AA',
            name = 'Amphi A',
            capacity = 100,
            location = 'EPL',
            availability = 'yes', 
            etat = 'Libre'
        )
        classroom.save()

        # Check new post saved
        all_classroom = Classroom.objects.all()
        self.assertEquals(len(all_classroom), 1)
        
        # Fetch the index
        response = self.client.get('http://127.0.0.1:8000/apis/classroom/5')
        self.assertEquals(response.status_code, 200)

        # Check the post title is in the response
        # self.assertTrue((classroom.codeClass).encode() in response.content)

        # Check the classroom text is in the response
        self.assertTrue(classroom.name in response)

        # Check the classroom name is in the response
        self.assertTrue(classroom.name in response.content)
        self.assertTrue(classroom.location in response.content)
        self.assertTrue(str(classroom.capacity) in response.content)
        
    def tearDown(self):
        return super().tearDown()
    
        
#ANCIEN TEST

# from django.test import TestCase

# from django.urls import reverse
# from rest_framework import status

# from ..models import Classroom
# from accounts.models import CustomUser
# # Create your tests here.

# class ClassroomTest(TestCase):
#     @classmethod
    
#     def setUp(self):        # creation des données de test pour chaque méthode de test
#         self.user = CustomUser.objects.create(
#             username = "testuser",
#             name = "Tested User",
#             email = "testuser@gmail.com",
#             address = ""
#         )
        
#         self.classroom = Classroom.objects.create(
#             codeClass = 'AA',
#             name = 'Amphi A',
#             capacity = 100,
#             location = 'EPL',
#             availability = 'yes', 
#             etat = 'Libre'
#         )
        
#     def test_classroom_content(self):         # Vérifie que les données sont correctes
#         self.client.force_login(self.user)
        # self.assertEqual(self.classroom.codeClass, 'AA')
        # self.assertEqual(self.classroom.name, 'Amphi A')
        # self.assertEqual(self.classroom.capacity, 100)
        # self.assertEqual(self.classroom.location, 'EPL')
        # self.assertEqual(self.classroom.availability, 'yes')
        # self.assertEqual(self.classroom.etat, 'Libre')
        
#     def test_classroom_listview(self):        # Vérifie que la vue de liste affiche correctement les salles
#         self.client.force_login(self.user)
#         response = self.client.get(reverse('list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, 'Amphi A')
#         self.assertTemplateUsed(response, 'list.html')
        
#     def test_classroom_detail(self):         # Vérifie que la vue de détail affiche correctement les détails des salles
#         self.client.force_login(self.user)
#         response = self.client.get(
#             reverse("detail", kwargs={"pk": self.classroom.id}),
#             format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Classroom.objects.count(), 1)
#         self.assertContains(response, 'Amphi A')   
        