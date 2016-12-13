from django import forms
from mysite.models import *
from mysite.models import *

# our contact form
class ContactEmailForm(forms.Form):
	#options=(("Python","Python"),("Django","Django"),("Ruby","Ruby"),("php","php"),("Unix","Unix"))
	name = forms.CharField(required=True)
 	email = forms.EmailField(required=True)
	#course=forms.ChoiceField(choices=options)
	course = forms.ModelChoiceField(queryset=Course_Database_Mail.objects.all())
 	phone = forms.CharField(required=True, max_length=12)
 	message = forms.CharField(required=True, widget=forms.Textarea)


class Pop_Up_Form(forms.Form):
	name=forms.CharField(required=True,label="Name")
	phone=forms.CharField(required=True,label='Phone')
	email=forms.EmailField(required=True,label='Email')
	course=forms.CharField(required=True,label="Course")


class ContactEmailForm_Popup(forms.Form):
	name = forms.CharField(required=True,label='Name')
	phone=forms.CharField(required=True,label='Phone')
	email=forms.EmailField(required=True,label='Email')
 	course = forms.CharField(required=True,label='Course')

