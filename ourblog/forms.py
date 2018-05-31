from django import forms
from ourblog.models import Blog, Comment, Blogger
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ("title", "blog_text", "blog_image", "publish_date")

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')

class BloggerForm(forms.ModelForm):

    class Meta:
        model = Blogger
        fields = ("name", "info", "profile_image", "place_from", "university_name", "course_name")

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user
