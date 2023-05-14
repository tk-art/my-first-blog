from django import forms
from .models import CustomUser


class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields =['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
