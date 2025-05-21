from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permissions_class = (AllowAny,)
    serializer_class = RegisterSerializer
