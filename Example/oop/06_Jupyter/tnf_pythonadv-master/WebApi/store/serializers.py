from django.contrib.auth.models import User
from rest_framework import fields, serializers
from .models import Composer, Compilation

class ComposerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composer
        fields = ['id', 'firstname', 'lastname']
        
class CompilationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compilation
        fields = ['id', 'title', 'artists']
        
class UserSerializer(serializers.ModelSerializer):
    composers = serializers.PrimaryKeyRelatedField(many=True, queryset=Composer.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'composers')