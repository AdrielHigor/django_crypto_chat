from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.core import models as core

class RegistrationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': "As senhas não coincidem.",
    }

    password1 = forms.CharField(label="Senha",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar senha",
        widget=forms.PasswordInput,
        help_text="Repita a senha para a verificação.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
        
    class Meta:
        model = core.User
        fields = ('username', 'email')

class AuthenticationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = core.User
        fields = ('username', 'password')
