from django.views import View
from django import forms
from django.contrib.auth import password_validation
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib import messages

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','phone','email','locality','city','state']
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'phone':forms.NumberInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.TextInput(attrs={'class':'form-control'})
        }

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html',{'form':form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            reg = Customer(first_name=first_name,last_name=last_name,
            phone=phone, email=email,locality=locality,city=city,state=state)
            reg.save()
            messages.success(request, 'Congratulations !! Profile Updated Successfully ')
        return render(request, 'profile.html' , {'form':form, 'active':'btn-primary'} )
            
            

