from .models import ItemsForSale,ItemImage
from rest_framework import serializers
from .models import ItemImage,ItemsForSale


class PostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemsForSale
        fields="__all__"
        read_only_fields=['user']

    def create(self, validated_data):
        user = self.context['request'].user
        return ItemsForSale.objects.create(user=user, **validated_data)    

class PostItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemImage
        fields="__all__"
        read_only_fields=['item']
