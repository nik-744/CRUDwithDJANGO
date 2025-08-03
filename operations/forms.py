from django import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['firstName', 'lastName', 'email', 'age', 'department']
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }