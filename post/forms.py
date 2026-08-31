from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'sended_message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangiz'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998901234567'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}),
            'sended_message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Xabar matni...'}),
        }