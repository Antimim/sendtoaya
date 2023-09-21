from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    pwd = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    pwd = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    pwd_confirm = forms.CharField(
        label="Mot de Passe de confirmation",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
