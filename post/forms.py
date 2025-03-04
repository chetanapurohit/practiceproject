from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, Post
 

class SignupForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_no', 'email']
        labels = {'email':'Email'}

    def clean(self):
        cleaned_data = super().clean()  
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
