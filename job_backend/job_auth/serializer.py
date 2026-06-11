## create the serializer for authentication
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import *




# --------------------------
# user Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']


# RegisterSerializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    ## unaweza kuadd na fields zinginze za user-profile
    phone = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = '__all__' 

    
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        ## incase ukawa na fields za profiles
        phone = validated_data.pop('phone')
        address = validated_data.pop('address')

        user = User(
            username = validated_data['username'],
            role = validated_data['role']
        )

        user.set_password(validated_data['password'])
        user.save()

        UserProfile.objects.create(user=user, phone=phone, address=address)
        return user

