from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
	email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Email'}))
	telephone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Dejanos tu mensaje!'}))