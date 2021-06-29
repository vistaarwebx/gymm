from .serializers import zContactSerializer
from django.shortcuts import render
from .models import contactss
from rest_framework import viewsets

class ContacttModelViewSet(viewsets.ModelViewSet):
    queryset = contactss.objects.all()
    serializer_class = zContactSerializer