 from django import forms
 from dealing.models import*
 

class contactform(form.ModelForm):
	class Meta:
		model=contact
		field='_all_'
