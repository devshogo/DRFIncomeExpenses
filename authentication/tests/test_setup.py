import faker
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        # self.logout_url = reverse('logout-list')

        self.fake = Faker()


        # self.user_data = {
        #     'email':"john@gmail.com",
        #     'username':"john",
        #     'password': "@email123"
        # }

        self.user_credentials = {
            'email':"john@gmail.com",
            'password': "@email123"
        }

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),
        }

        

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    

