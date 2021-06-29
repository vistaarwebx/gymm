from rest_framework import serializers
from .models import contactss

class zContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contactss
        fields = ['id', 'url', 'name', 'subject', 'Email', 'Address']