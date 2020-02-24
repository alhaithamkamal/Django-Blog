from __future__ import unicode_literals
from django.db import models
from  django.contrib.auth.models import User
from  django.utils import timezone
from  django.urls import reverse

# Create your models here.
class Post(models.Model):
	STATUS_CHOICES =(
		('draft', 'Draft'),
		('published', 'Published'),
)

	title = models.CharField(max_length = 200)
	slug = models.SlugField(max_length = 200)
	image = models.FileField(null=True, blank=True)
	body = models.TextField()
	user = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='blog_posts')
	published = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length = 200,choices= STATUS_CHOICES, default='draft')
	likes = models.ManyToManyField(User, related_name='likes', blank=True)
	restrict_comment = models.BooleanField(default=False)



	class Meta:
		ordering = ('-created',)

	def __unicode__(self):
		return self.title
		


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:post_detail', args=[self.id])
	





class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
	content = models.TextField(max_length=300)
	approved = models.BooleanField(default=False)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return  '{} commented on {}.'.format(str(self.user.username), self.post.title)
					
	