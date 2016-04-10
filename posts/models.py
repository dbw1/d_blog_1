from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=120)  #max_length = 120
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) #1st time made initially
	updated = models.DateTimeField(auto_now=True, auto_now_add=False) #everytime it's updated
	  #auto_now is every time your post is saved in db, updated will be set
	  #auto_now_add is 
	def __str__(self):
		return self.title

	# for python 2
	#def __unicode__(self):
	#	return self.title
