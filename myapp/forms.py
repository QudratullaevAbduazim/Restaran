from django import forms
from .models import Food
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price', 'desc', 'image']
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError('Narxni togri kiriting')
        return price