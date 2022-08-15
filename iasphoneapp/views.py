from django.shortcuts import render
from iasphoneapp.models import Person
from iasphoneapp.serializers import PersonSerializer
from rest_framework import viewsets

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
