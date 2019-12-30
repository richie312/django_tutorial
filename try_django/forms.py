from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.CharField()
	context = forms.CharField(widget = forms.Textarea)