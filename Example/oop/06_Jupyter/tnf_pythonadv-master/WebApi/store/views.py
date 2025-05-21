from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Composer, Compilation
from .serializers import CompilationSerializer, ComposerSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class ComposerViewSet(ListAPIView):
    queryset = Composer.objects.all()
    serializer_class = ComposerSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        
class ComposerCreate(CreateAPIView):
    queryset = Composer.objects.all()
    serializer_class = ComposerSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()
        
class ComposerUpRetDel(RetrieveUpdateDestroyAPIView):
    queryset = Composer.objects.all()
    serializer_class = ComposerSerializer
    permission_classes = [IsAuthenticated]
