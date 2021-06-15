from django import forms
# from authentication.models import Uzer


class CreateTicket(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
