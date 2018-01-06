from django import forms
from .models import Values

class DataForm(forms.ModelForm):

    class Meta:
        model = Values
        fields = ('name', 'position', 'office', 'age', 'salary',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'office': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
        }
