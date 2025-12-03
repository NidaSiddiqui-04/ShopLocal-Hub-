from django.test import TestCase
from accounts.models import CustomUser


class UserModelTest(TestCase):
    def test_create_user(self):
        username="test user"
        phone_number="0000000001"
        password="test@123"

        user=CustomUser.objects.create_user(username=username,phone_number=phone_number,password=password)

        self.assertEqual(user.phone_number,phone_number)
        self.assertEqual(user.username,username)
        self.assertTrue(user.check_password(password))
