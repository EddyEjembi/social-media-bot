from django import forms

class Client(forms.Form):
    profile_name = forms.CharField(required=False)
    post_link = forms.URLField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)
