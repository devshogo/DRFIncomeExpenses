import email
from http import client
from turtle import pd
from unittest import result
from .test_setup import TestSetUp
from ..models import User

class TestViews(TestSetUp):

    def test_user_cannot_register_without_data(self):
        res = self.client.post(self.register_url)
        result = res.status_code
        import pdb
        # pdb.set_trace()
        self.assertEqual(result, 400)

    def test_user_can_register_successfully(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        result = res.status_code
        import pdb
        # pdb.set_trace()
        self.assertEqual(result, 201)

    def test_user_cannot_login_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        result = res.status_code
        import pdb
        # pdb.set_trace()
        self.assertEqual(result, 401)

    def test_user_can_login_after_email_verification(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = User.objects.get(email = email)
        user.is_active = True
        user.is_verified = True     
        user.save()

        res = self.client.post(self.login_url, self.user_data, format="json")
        result = res.status_code       
        import pdb
        pdb.set_trace()
        self.assertEqual(result, 200)

    # def test_user_can_logout(self):
    #     self.client.post(self.logout_url, self.user_data, format="json")
    #     res = self.client.post(self.logout_url, self.user_credentials, format="json")
    #     result = res.status_code
    #     import pdb
    #     # pdb.set_trace()
    #     self.assertEqual(result, 401)

    # def test_user_can_logout(self):
    #     response = self.client.post(self.register_url, self.user_data, format="json")
    #     email = response.data['email']
    #     user = User.objects.get(email = email)
    #     user.is_active = True
    #     user.save()
    #     res = self.client.post(self.login_url, self.user_credentials, format="json")
    #     refresh_token = res.data['refresh']

    #     res_logout = self.client.post(self.logout_url, self.user_credentials, format="json")

        
    #     result = res_logout.status_code
    #     # print(refresh_token)       
    #     import pdb
    #     # pdb.set_trace()
    #     self.assertEqual(result, 200)