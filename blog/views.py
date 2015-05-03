from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogContent
from blog import forms

def index(request):
	blog_posts = BlogContent.objects.all()

	return render(request, 'blog/home.html', { 'blog_posts': blog_posts })

def contact(request):
	if request.method == 'POST':
		pass
	else:
		form = forms.ContactForm(auto_id=False)
		
	return render(request, 'blog/contact.html', {'form':form})

