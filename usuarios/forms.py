from django import forms
from usuarios.models import User

class CreateUserForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico")
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    phone= forms.CharField(label="Teléfono")
    password1 = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, required=False
    )
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput, required=False
    )
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone", "password1", "password2"]

    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError("Las contrasenas no coinciden")

    def save(self, commit=True):
        # Save the provided password in hashed format
        password = self.cleaned_data.get("password1")
        confirm_password = self.cleaned_data.get("password2")
        user = super(CreateUserForm, self).save(commit=False)
        if password and confirm_password:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico")
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    phone= forms.CharField(label="Teléfono")
    old_password = forms.CharField(
        label="Contraseña actual", widget=forms.PasswordInput, required=False
    )
    password1 = forms.CharField(
        label="Nueva Contraseña", widget=forms.PasswordInput, required=False
    )
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput, required=False
    )
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone", "password1", "password2"]

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")
        if (old_password or new_password or confirm_password) and not (old_password and new_password and confirm_password):
            raise forms.ValidationError("Las contrasenas no coinciden")

        if new_password != confirm_password:
            raise forms.ValidationError("Las contrasenas no coinciden")

        user = User.objects.get(email=cleaned_data.get("email"))
        if old_password and not user.check_password(old_password):
            raise forms.ValidationError("Contraseña antigua incorrecta")

    def save(self, commit=True):
        # Save the provided password in hashed format
        password = self.cleaned_data.get("password1")
        confirm_password = self.cleaned_data.get("password2")
        user = super(EditUserForm, self).save(commit=False)
        if password and confirm_password:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user