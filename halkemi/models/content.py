from django.db import models
from halkemi.models.category import Category
from django.contrib.auth.models import User

class Content(models.Model):

	user_id = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	content = models.TextField()
	pic_link = models.TextField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = 'hali_db_content'

	def __unicode__(self):
		return self.content