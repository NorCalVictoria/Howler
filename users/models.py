from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	clip = models.FileField(upload_to='user_video/', null=True, verbose_name="VID") # upload video
	name = models.CharField(max_length=500, default='name_default')
	image = models.ImageField(max_length=100, upload_to='post_pic/', null=True, blank=True, width_field="width_field", height_field="height_field", default="tunnel.png")
	height = models.IntegerField(default=0)         # FileField requires validation ImageField , not
	width = models.IntegerField(default=0)
	def __str__(self):								
		return self.name + " : " + str(self.clip)

	def __str__(self):
		return self.name +":"+ str(self.image)
	def get_absolute_url(self):
		return reverse('image:detail', kwargs={'pk'.pk})




class PostContent(models.Model):
	imagePost = models.FileField(default='default.jpg', upload_to='post_pics', null=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):								
		return self.author + " : " + str(self.imagePost) 
 


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.FileField(default='default.jpg', upload_to='profile_pics')
	# bio = models.TextField(max_length=500, blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 600)
			img.thumbnail(output_size)
			img.save(self.image.path)
