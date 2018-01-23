from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
