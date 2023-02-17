from xml.dom import ValidationErr
from django import forms
from .models import *


def validate_uzb_number(value):
    if not value[1:].isdigit():
        raise ValidationErr('Only digits allowed')
    if len(value) != 12:
        raise ValidationErr('Must contain 13 digits') 


class CallbackForm(forms.ModelForm):
    phone = forms.CharField(validators=[validate_uzb_number,], widget=forms.NumberInput(attrs={
                'placeholder': '(__) ___-__-__'}))
    class Meta: 
        model = Callback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Full Name'}
            ),
            'phone': forms.NumberInput(attrs={
                'placeholder': '(__) ___-__-__',
                # 'id': 'phone-number',
                # 'type': 'tel'
                }
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

