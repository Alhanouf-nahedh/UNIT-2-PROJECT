from django import forms
from .models import Message

# Form for the contact page
class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'content']