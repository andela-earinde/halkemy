from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'name','placeholder':'Name'}),
    max_length=100)

	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email'}), 
    max_length=100)

	phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','id':'phone','placeholder':'Phone'}),
    max_value=11)

	messages = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','id':'message','placeholder':'Message'}))