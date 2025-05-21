from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Composer, Compilation
from .serializers import CompilationSerializer, ComposerSerializer

# Create your views here.
class ComposerViewSet(viewsets.ModelViewSet):
    queryset = Composer.objects.all()
    serializer_class = ComposerSerializer