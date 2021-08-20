from django import forms
from django.forms import fields
from .models import ContactFormModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]