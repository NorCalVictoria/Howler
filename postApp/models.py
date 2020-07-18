from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	clip = models.FileField(upload_to='user_video/', null=True) # upload video

	def __str__(self):
		return self.title

	

	#return the url as a string to give to views
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})