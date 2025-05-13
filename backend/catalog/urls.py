
from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.categoryList, name="catergoryList"),
    path('items/', views.itemList, name="itemList"),
]

