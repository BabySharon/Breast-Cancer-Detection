from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userModel, Patient

class SignIn(UserCreationForm):
    # username = forms.CharField(max_length=100,
    # widget = forms.TextInput(attrs={"placeholder":'Name'}))
    name = forms.CharField(max_length=200,
    widget = forms.TextInput(attrs={'placeholder':'Name'}))
    institution = forms.CharField(max_length=200,
    widget = forms.TextInput(attrs={'placeholder':'Name of Institution'}))
    # password1 = forms.CharField(max_length=32,
    # widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    # password2 = forms.CharField(max_length=32,
    # widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username','name','institution','password1','password2']
        # fields=[
        #      'institution'
        # ]
        # widgets={
        #     'username' : forms.TextInput(attrs={"placeholder":'Name'}),
        #     'password1' : forms.PasswordInput(attrs={'placeholder':'Password'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder':'Confirm Password'})
        # }


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['pname','age','testfile']
        widgets = {
            'pname': forms.TextInput(attrs={'placeholder':'Patient Name'}), 'age' : forms.NumberInput(attrs={'placeholder':'Age'}), 
        }
