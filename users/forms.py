from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)




class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
                 'username',
                 'first_name',
                 'last_name',
                 'email',
                 'is_superuser',
                 'is_staff'
                )
        
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            'is_superuser',
            'is_staff'
            ]
        
class ResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    password_confrim = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    
    
class edit_userForm(forms.Form):
    email = forms.CharField(label="ایمیل جدید")
    username = forms.CharField(label="نام کاربری جدید")
    
from courses.models import *
    
class HandoutForm(forms.ModelForm):
    other_files = forms.FileField(required=False, label='فایل های دیگر جزوه')
    class Meta:
        model = Handout
        fields = '__all__'
        

class PictureForm(forms.Form):
    image = forms.ImageField()