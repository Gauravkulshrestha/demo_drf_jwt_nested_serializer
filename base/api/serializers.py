from django.forms import ValidationError
from rest_framework import serializers
from .models import Company, Mobile
from django.contrib.auth.models import User

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id','mobile_name', 'model_name', 'price', 'description', 'company_name']

class CompanySerializer(serializers.ModelSerializer):
    by = MobileSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id','name', 'by']

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)        
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        extra_kwargs = {
        'password1':{'write_only':True},
        'password2':{'write_only':True}        
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password1 = validated_data['password1']
        password2 = validated_data['password2']
        user = User(username=username, email=email)
        if password1 == password2:
            user.set_password(validated_data['password1'])
            user.save()                        
            return user
        else:
            raise serializers.ValidationError({
            'error':'Password does not match!'
        })