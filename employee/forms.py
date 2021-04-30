from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

#Sign Up form
class SignUpFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    number = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'number', 'password1', 'password2']

