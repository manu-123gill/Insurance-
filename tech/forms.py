from django import forms
from tech.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class customerform(forms.ModelForm):
	class Meta:
		model=saveform
		fields='__all__'
        
class contactform(forms.ModelForm):
	class Meta:
		model=contact
		fields='__all__'

class loginform(UserCreationForm):
     class Meta:
            model=User
            fields=('email','username','password1','password2',)

class registerform(forms.ModelForm):
    class Meta:
        model=registrationform
        fields='__all__'
        
class loginform(UserCreationForm):
    class Meta:
        model=User
        fields=('email','username','password1','password2',)
    
class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=('email','username','password1','password2',)