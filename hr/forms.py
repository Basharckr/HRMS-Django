from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AddEmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placehoder': 'Enter password'
    }))


    class Meta:
        model = User
        fields = '__all__'

