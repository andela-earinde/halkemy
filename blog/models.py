import datetime
from django.db import models
from django.utils import timezone

class BlogContent(models.Model):
	blog_heading = models.CharField(max_length=200)
	blog_subheading = models.CharField(max_length=200)
	blog_pub_date = models.DateTimeField('date blog published')
	blog_content = models.TextField('blog content')

	def was_published_recently(self):
		now = timezone.now()
		return now-datetime.timedelta(days=1)<=self.blog_pub_date<=now

	def __unicode__(self):
		return self.blog_heading
