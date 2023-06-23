from django import forms
from .models import CustomUser, Item


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
    text = forms.CharField(widget=forms.Textarea)
    # 他の必要なフィールドを追加する
