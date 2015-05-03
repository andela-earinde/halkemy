from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def is_unique_username(value):
	user = User.objects.filter(username__iexact=value)

	if user:
		raise ValidationError(u'the username %s is already taken' %value)

def is_unique_email(value):
	email = User.objects.filter(email__exact=value)

	if email:
		raise ValidationError(u'the email %s is already taken' %value)