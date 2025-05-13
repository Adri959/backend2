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

@api_view(["GET","POST"])
def itemList(request):
    if request.method== "GET":  
        allItems = Item.objects.all().order_by('-uploadDate')
        serialized = ItemSerializer(allItems,many = True)
        return Response(serialized.data)
    
    if request.method== "POST":
        serialized = ItemSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status.HTTP_201_CREATED)
        return Response(serialized.errors,status.HTTP_400_BAD_REQUEST)
    
@api_view(["DELETE"])
def deleteItem(request,itemId):
    if(request.method=="DELETE"):
        currentItem = Item.objects.get(pk=itemId)
        currentItem.delete()
        return Response(currentItem.data,status.HTTP_200_OK)

    
