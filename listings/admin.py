from django.contrib import admin
from .models import ItemImage,ItemsForSale
# Register your models here.
admin.site.register(ItemsForSale)
admin.site.register(ItemImage)