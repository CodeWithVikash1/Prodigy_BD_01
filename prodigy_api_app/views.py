from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
# Create your views here.

class user_list(generics.ListCreateAPIView):
    queryset = Userlist.objects.all()
    serializer_class = UserSerializer
    
class user_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userlist.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'