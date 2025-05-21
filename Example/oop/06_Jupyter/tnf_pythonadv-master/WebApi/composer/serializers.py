from rest_framework import fields, serializers
from .models import Composer, Compilation

class ComposerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composer
        fields = ['firstname', 'lastname']
        
class CompilationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compilation
        fields = ['title', 'artists']