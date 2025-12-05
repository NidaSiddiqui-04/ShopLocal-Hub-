from django.test import TestCase
from listings.models import ItemsForSale,ItemImage
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


class PostItemWithImageTest(TestCase):
    def test_posts(self):
        user=CustomUser.objects.create_user(username="test user",phone_number="00000001",password="test@123")    
        items=ItemsForSale.objects.create(title="test item",price=678,user=user) 
        post= ItemImage.objects.create(item=items,caption="test caption")
        post1=ItemImage.objects.create(item=items)
        post2=ItemImage.objects.create(item=items)
        post3=ItemImage.objects.create(item=items)
        post4=ItemImage.objects.create(item=items)

        self.assertIsNotNone(post.item)

        self.assertIsNotNone(post1.item)
        self.assertIsNotNone(post2.item)
        self.assertIsNotNone(post3.item)
        self.assertIsNotNone(post4.item)

