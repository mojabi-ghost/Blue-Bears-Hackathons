
from django import forms
from . models import Register, Account
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'university', 'major']
        
class AccountAuthenticationForm(forms.ModelForm):
    
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")

