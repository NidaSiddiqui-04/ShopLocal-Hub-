from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# Create your models here.
class ItemsForSale(models.Model):
    CATEGORY_CHOICES=[("1","Electronic"),("2","Furniture"),("3","vechicle")]
    CONDITION_CHOICES=[("NEW","New"),('Like New',"Like New"),("Good","Good"),("Used","Used")]
    STATUS_CHOICES=[("Available","Available"),("Sold","Sold")]
    title =models.CharField(max_length=200)
    description =models.TextField(null=True,blank=True)
    price=models.FloatField()
    category=models.CharField(choices=CATEGORY_CHOICES,default="none")
    condition=models.CharField(choices=CONDITION_CHOICES,default="Good")
    user=models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="items")
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,default="Available")
    image = models.ImageField(upload_to='products',default="media.png")



    def __str__(self):
        return f"{self.title}-{(self.user.username)}"


