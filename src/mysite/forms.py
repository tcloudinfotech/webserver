from django import forms
from mysite.models import *

# our contact form
class ContactEmailForm(forms.Form):
	name = forms.CharField(required=True)
 	email = forms.EmailField(required=True)
	course = forms.ModelChoiceField(queryset=Course.objects.all())
 	phone = forms.CharField(required=True, max_length=12)
 	message = forms.CharField(required=True, widget=forms.Textarea)


# this form is getting called in the Pop_Up_view views.
class Pop_Up_Form(forms.Form):
	name=forms.CharField(required=True,label="Name")
	phone=forms.CharField(required=True,label='Phone')
	email=forms.EmailField(required=True,label='Email')
	course=forms.CharField(required=True,label="Course")

# this form is getting called in the Contact_View_Popup views.
class ContactEmailForm_Popup(forms.Form):
	name = forms.CharField(required=True,label='Name')
	phone=forms.CharField(required=True,label='Phone')
	email=forms.EmailField(required=True,label='Email')
 	course = forms.CharField(required=True,label='Course')
