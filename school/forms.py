from .models import User
from django.forms import ModelForm, NumberInput,TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['pirmdiena', 'otrdiena', 'tresdiena', 'ceturdiena', 'piektdiena', 'apestasporcijas', 'skolenuskaits']

        widgets = {
            "pirmdiena":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pirmdiena'
            }),
            "otrdiena":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Otrdiena'
            }),
              "tresdiena":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Trešdiena'
            }),
             "ceturdiena":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ceturdiena'
            }),
             "piekdiena":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Piektdiena'
            }),
            "apestasporcijas":NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
            "skolenuskaits":NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
            
            
        }