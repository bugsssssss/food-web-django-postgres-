from django import forms
from .models import *

class CallbackForm(forms.ModelForm):
    
    class Meta: 
        model = Callback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Full Name'}
            ),
            'phone': forms.NumberInput(attrs={
                'placeholder': 'Phone Number'}
            ),
            'message': forms.TextInput(attrs={
                'class': 'message_input',
                'placeholder':"Message"
                }
            ),
        }



class FoodModelForm(forms.ModelForm):
    
    class Meta:
        model = FoodModel
        fields = ("quantity",)

