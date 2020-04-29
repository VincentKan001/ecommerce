from django import forms
from .models import Product
from pyuploadcare.dj.forms import ImageField

class NewProduct(forms.ModelForm):
    class Meta:
        model = Product        
        fields = (
            'name',
            'sku',
            'description',
            'cost',
            'quantity',
            'photo'
        )