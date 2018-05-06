from django import forms
from .models import Values
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class DataForm(forms.ModelForm):

    class Meta:
        model = Values
        fields = ('pressure', 'temperature', 'ph', 'levels',)
        widgets = {
            'pressure': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'ph': forms.TextInput(attrs={'class': 'form-control'}),
            'levels': forms.TextInput(attrs={'class': 'form-control'}),
        }
