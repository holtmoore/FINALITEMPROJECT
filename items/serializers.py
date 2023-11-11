from .models import Item
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id','title', 'description', 'amount', 'type']