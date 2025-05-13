from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

# Create your views here.

@api_view(["GET"])
def categoryList(request):
    allCategories = Category.objects.all().order_by("categoryName")
    serialized = CategorySerializer(allCategories,many=True)
    return Response(serialized.data)

@api_view(["GET"])
def itemList(request):
    allItems = Item.objects.all().order_by('-uploadDate')
    serialized = ItemSerializer(allItems,many = True)
    return Response(serialized.data)
