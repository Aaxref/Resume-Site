from django import forms
from .models import Message

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="نام", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="پیام", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['response']