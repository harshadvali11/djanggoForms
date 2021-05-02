from django import forms

class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(max_value=80,min_value=18)

