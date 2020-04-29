from django.urls import path, include
from .views import catalog, add_product

urlpatterns = [
    path('', catalog, name='catalog'),
    path('add_product/', add_product , name='add_product'),
   
]