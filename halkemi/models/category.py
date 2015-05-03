from django.db import models

class Category(models.Model):
	choice = (('fashion', 'fashion'),
              ('food', 'food'),
              ('art & photography', 'art & phoyography'),)

	category_name = models.CharField(max_length=100, choices=choice)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField() 


	class Meta:
		db_table = 'hali_db_category'

	def __unicode__(self):
		return self.category_name