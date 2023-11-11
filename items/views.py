# from django.shortcuts import render
from .models import Item
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]
    