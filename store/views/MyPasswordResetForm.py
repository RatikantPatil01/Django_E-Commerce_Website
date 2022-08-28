import email
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation
from django.shortcuts import render, redirect
from store.views import passwordchange
from django.contrib.auth.forms import PasswordResetForm


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=("Email"), max_length=254,
    widget=forms.EmailInput(attrs={'autocomplete':'email',
    'class':'form-control'}))