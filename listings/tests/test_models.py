from django.test import TestCase
from listings.models import ItemsForSale
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

class ItemsPostTest(TestCase):
    def test_items_posts(self):
        title="test item"
        price=678
        user=CustomUser.objects.create_user(username="test user",phone_number="000000001",password="test@12345")

        items=ItemsForSale.objects.create(title = title,price=price,user=user)

        self.assertEqual(items.title,title)
        self.assertEqual(items.price,price)
        self.assertIsNotNone(items.status)
        self.assertIsNotNone(items.category)


