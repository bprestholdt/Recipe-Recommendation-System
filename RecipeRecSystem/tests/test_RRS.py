import os
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
import django

class RRSystemTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        os.environ['DJANGO_SETTINGS_MODULE'] = 'RecipeRecSystem.settings'
        django.setup()

    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )

    def test_homepage_access(self):
        # Log in with the test user
        self.client.login(username='test_user', password='test_password')

        response = self.client.get(reverse('home'))

        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)