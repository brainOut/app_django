from django import forms
from hashlib import sha256
from django.conf.global_settings import SECRET_KEY


class ProjectForm(forms.Form):
    wd = forms.TextInput(attrs={'size': 50})
    name = forms.CharField(required=True, max_length="100", widget=wd)
    url = forms.CharField(required=True, max_length="300", widget=wd)
    token = forms.CharField(required=True, max_length="300", widget=wd)

    def hash_token(self):
        self.cleaned_data["token"] = sha256(f"{self.cleaned_data['token'] + SECRET_KEY}".encode()).hexdigest()
