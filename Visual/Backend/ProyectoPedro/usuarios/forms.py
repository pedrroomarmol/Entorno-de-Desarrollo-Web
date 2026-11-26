from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico", required=True)

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
