from django import forms
from django.contrib.auth.models import User

class Signupform(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password','email','first_name','last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'user',
                'required': True,
                'placeholder': 'Username'
            }),
            }

class Forgot_pwd(forms.Form):
    Username=forms.CharField()
    Email=forms.EmailField()
