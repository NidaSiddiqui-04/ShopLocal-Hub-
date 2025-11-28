
from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "password2",
            "phone_number",
            "email",
            "name",
            "image",
            "address",
        ]
        extra_kwargs = {
            "email": {"required": False, "allow_null": True, "allow_blank": True},
            "name": {"required": False, "allow_null": True, "allow_blank": True},
            "image": {"required": False, "allow_null": True},
            "address": {"required": False, "allow_null": True, "allow_blank": True},
        }

    def validate(self, attrs):
       
        if attrs["password"]!=  attrs["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")  
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["username","image","address","email","phone_number","name"]
        read_only_fields=('username',"phone_number")