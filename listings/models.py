from django.db import models
from django.conf import settings

# Create your models here.

class ItemsForSale(models.Model):
    CATEGORY_CHOICES=[("1","Electronic"),("2","Furniture"),("3","vechicle")]
    CONDITION_CHOICES=[("NEW","New"),('Like New',"Like New"),("Good","Good"),("Used","Used")]
    STATUS_CHOICES=[("Available","Available"),("Sold","Sold")]
    title =models.CharField(max_length=200)
    description =models.TextField(null=True,blank=True)
    price=models.PositiveIntegerField()
    category=models.CharField(choices=CATEGORY_CHOICES,default="none")
    condition=models.CharField(choices=CONDITION_CHOICES,default="Good")
    user=models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="items")
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,default="Available")
    


    def __str__(self):
        return f"{self.title}-{(self.user.username)}"




class ItemImage(models.Model):
    item = models.ForeignKey(
        ItemsForSale,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to='media',default="media.png")
    # optionally, you can add a caption or order:
    caption = models.CharField(max_length=200, blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.item.title}"