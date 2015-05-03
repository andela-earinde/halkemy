from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
	user = models.OneToOneField(User)
	skill = models.CharField(max_length=100)
	description = models.TextField()
	profile_pic = models.TextField()
	pic_small = models.TextField()

	class Meta:
		db_table = 'hali_db_user'

	def __unicode__(self):
		return self.skill
