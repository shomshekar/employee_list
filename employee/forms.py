from django import forms

# Create the FormName class
class FormName(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()