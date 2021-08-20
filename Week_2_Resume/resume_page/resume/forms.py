from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=30)
    message = forms.CharField(max_length=300)