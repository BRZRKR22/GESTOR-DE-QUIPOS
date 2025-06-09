from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(choices=[('usuario', 'Usuario Normal'), ('administrador', 'Administrador')], required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'rol']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            rol = self.cleaned_data['rol']
            group = Group.objects.get(name=rol)
            user.groups.add(group)
        return user
