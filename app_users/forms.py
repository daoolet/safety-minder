from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


from .models import CustomUser

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'position', 'area', 'line_manager')

        
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'badge', 'position', 'area', 'line_manager')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser