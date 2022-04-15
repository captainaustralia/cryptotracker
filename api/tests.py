from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import User, Portfolio


class RegisterTests(APITestCase):
    def test_create_account(self):
        """
        Register API endpoint testcase
        """
        url = reverse('register')
        data = {'email': 'test@mail.com', 'password': '123123', 'username': 'test1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@mail.com')


class PortfolioTests(APITestCase):
    def test_create_portfolio(self):
        """
        Create portfolio, but not auth / 401:401
        """
        url = reverse('create_portfolio')
        data = {'name': 'testportfolio'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Portfolio.objects.count(), 0)

    def test_create_portfolio_auth(self):
        pass
