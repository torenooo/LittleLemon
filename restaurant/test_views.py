from django.test import TestCase, Client
from .models import Menu

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        # Create sample menu items for testing
        Menu.objects.create(title="Burger", price=9.99, inventory=20)
        Menu.objects.create(title="Fries", price=3.49, inventory=50)

    def test_menu_view_response_status(self):
        response = self.client.get('/restaurant/menu/')  # Using the URL directly
        self.assertEqual(response.status_code, 200)

    def test_menu_view_returns_data(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['title'], 'Burger')
