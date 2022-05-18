from .models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['pirmdiena', 'otrdiena', 'tresdiena', 'ceturdiena', 'piekdiena']