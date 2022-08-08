from django import forms
from .models import Feedback

class FeedbackForms(forms.Form):

    name_field = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control footer-input margin-b-20'}))
    email_field = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control footer-input margin-b-20'}))
    phone_field = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control footer-input margin-b-20'}))
    message_field = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control footer-input margin-b-30', 'rows': 6}))
