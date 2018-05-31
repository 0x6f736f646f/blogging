from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fieldls = ("username", "email", "profile_image", "university_name", "course_name", "password1", "password2")

        def save(self, commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


class Changepassword(PasswordChangeForm):
    
