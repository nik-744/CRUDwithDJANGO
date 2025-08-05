from django import forms
from .models import student,department

class StudentForm(forms.ModelForm):
    gender= forms.ChoiceField(choices=[('','Select Gender')] + student.GENDER_CHOICES,widget=forms.Select(attrs={'class': 'form-control'}),required=True)
    
    department = forms.ModelChoiceField(
        queryset=department.objects.all(),
        empty_label="Select Department",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    class Meta:
        model = student
        fields = ['firstName', 'lastName', 'email', 'age','gender', 'department']
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class departmentForm(forms.ModelForm):
    class Meta:
        model= department
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'})
        }