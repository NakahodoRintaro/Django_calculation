from django import forms

class numForm(forms.Form):
  num1 = forms.DecimalField(label='A', initial=2, required=True)
  num2 = forms.DecimalField(label='B', initial=1, required=True)
