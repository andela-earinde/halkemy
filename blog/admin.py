from django.contrib import admin
from blog.models import BlogContent

class BlogContentAdmin(admin.ModelAdmin):
	"""docstring for BlogContentAdmin"""
	fieldsets = [(None, {'fields':['blog_heading']}),
                ('Blog subheading', {'fields':['blog_subheading']}),
                ('Publish Date', {'fields':['blog_pub_date']}),
                ('Blog content', {'fields':['blog_content']}),]

	list_display = ('blog_heading', 'blog_pub_date', 'was_published_recently')

	list_filter = ['blog_pub_date']


admin.site.register(BlogContent, BlogContentAdmin)