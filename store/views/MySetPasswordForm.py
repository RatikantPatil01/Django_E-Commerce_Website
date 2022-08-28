import email
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation
from django.shortcuts import render, redirect
from store.views import passwordchange
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=("New Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password', 'class':'form-control'}),
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm New Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete':'new-password','class':'form-control'}))