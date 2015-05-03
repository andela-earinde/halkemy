from django.shortcuts import render,redirect
from halkemi.forms import SignUpForm, LoginForm, EditProfileForm 
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

def index(request):
	return render(request, 'halkemi/index.html');


def signup(request):

	if request.method == 'POST':
		signup_form = SignUpForm(request.POST)
		if signup_form.is_valid():
			user = User()
			user.username = signup_form.cleaned_data['username']
			user.email = signup_form.cleaned_data['email']
			user.first_name = signup_form.cleaned_data['first_name']
			user.last_name = signup_form.cleaned_data['last_name']
			user.set_password(signup_form.cleaned_data['password'])
			user.save()
				
			return redirect(reverse('halkemi:login'))			
		else:
			return render(request, 'halkemi/signup.html', {'form':signup_form, 'message':'Please fill the form again'})
	    
	elif request.method == 'GET':
		signup_form = SignUpForm(auto_id=False)

		return render(request, 'halkemi/signup.html', {'form':signup_form})

def signin(request):

	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect(reverse('halkemi:profile'))
		else:
			return render(request, 'halkemi/login.html',{'form':login_form,'message':'invalid email address or password'})

	elif request.method == 'GET':
		login_form = LoginForm(auto_id=False)

		return render(request, 'halkemi/login.html', {'form': login_form})

def signout(request):
	logout(request)
	return redirect(reverse('halkemi:index'))

def profile(request):
	if request.method == "GET":
		return render(request, 'halkemi/profile.html')

def edit_profile(request):
	form = EditProfileForm(auto_id=False)
	if request.method == 'GET':
		return render(request, 'halkemi/edit_profile.html', {'form':form})

	elif request.method == 'POST':
		form = EditProfileForm(request.POST)
		if form.is_valid():
			pass
		else:
			return render(request, 'halkemi/edit_profile.html', {'form':form, 'message': 'Please retype the fields'})

def edit_profile_picture(request):
	pass



