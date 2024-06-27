from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autofocus':'True',
    'autocomplete':'current-password','class':'from-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={
    'autocomplete':'current-password','class':'from-control'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={
    'autocomplete':'current-password','class':'from-control'}))

class MyPasswordResetForm(PasswordChangeForm):
    pass 
class UserForm(forms.Form):
    name=forms.CharField(required=True,error_messages={'required':'please enter your name'})
    email=forms.EmailField(required=True,error_messages={'required':'please enter your email id'})


    