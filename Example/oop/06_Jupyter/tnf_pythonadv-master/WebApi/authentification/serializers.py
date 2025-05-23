from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import validators
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    passwordConfirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'passwordConfirm', 'email', 'first_name', 'last_name')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['passwordConfirm']:
            raise serializers.ValidationError({ 'password': 'Password filds must match!' })
         
        return attrs
    
    def create(self, validated_data):
        del validated_data['passwordConfirm']
        user = User.objects.create(**validated_data)
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user
