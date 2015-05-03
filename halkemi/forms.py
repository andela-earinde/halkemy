from django import forms
from django.core import validators
from halkemi import validator

class SignUpForm(forms.Form):
	
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
	                                                         'id':'login-username',
	                                                         'placeholder':'Username'}), max_length=30,
	                                                         validators=[validators.validate_slug,
	                                                         validator.is_unique_username])

	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
	                                                        'id':'login-username',
	                                                        'placeholder':'Email'}),
	                                                        validators=[validators.validate_email,
	                                                        validator.is_unique_email])
    
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
	                                                         'id':'login-username',	                                                       
	                                                         'placeholder':'First Name'}), max_length=30)

	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
	                                                         'id':'login-username',	                                                       
	                                                         'placeholder':'Last Name'}), max_length=30)


	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
	                                                         'id':'login-password',
	                                                         'name':'password',
	                                                         'placeholder':'Password'}))

	vpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
	                                                         'id':'login-password',
	                                                         'name':'password',
	                                                         'placeholder':'Retype Password'}))


	def clean(self):
		cleaned_data = super(SignUpForm, self).clean()
		password = cleaned_data.get('password')
		vpassword = cleaned_data.get('vpassword')

		if password and vpassword:
			if password != vpassword:
				msg = "retype password must be equal to password"
				self.add_error('vpassword', msg)


class LoginForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
	                                                        'id':'login-username',
	                                                        'name':'username',
	                                                        'placeholder':'Username'}),)

	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
	                                                         'id':'login-password',
	                                                         'name':'password',
	                                                         'placeholder':'Password'}),)

class EditProfileForm(forms.Form):

	skill = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
		                                                 'id':'Name',
		                                                 'name':'skill',
		                                                 'placeholder':'Skill'}), max_length=30)

	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
		                                                      'id':'contact-message',		                                                      
		                                                      'name':'description',
		                                                      'placeholder':'Description'}), max_length=200)

	                                                        
class EditProfilePicForm(forms.Form):

	profile_pic = forms.ImageField()


