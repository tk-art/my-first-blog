from django import forms
from .models import CustomUser, Item, Comment, Profile


class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'deadline', 'quantity', 'image']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'image', 'content']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
