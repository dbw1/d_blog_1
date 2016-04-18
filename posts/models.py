from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

#to save model changes
#python manage.py makemigrations <--like git add
#python manage.py migrate  <- like git commit

def upload_location(instance, filename):
	return "%s/%s" % (instance.id, filename) #sends media to that extension in media folder 

class Post(models.Model):
	title = models.CharField(max_length=120)  #max_length = 120
	slug = models.SlugField(unique=True) #must delete old db to make unique entries
	image = models.ImageField(upload_to = upload_location,
		null=True, 
		blank=True, 
		width_field="width_field", 
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) #1st time made initially
	updated = models.DateTimeField(auto_now=True, auto_now_add=False) #everytime it's updated
	  #auto_now is every time your post is saved in db, updated will be set
	  #auto_now_add is 
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})
		# reverse looks up name ="detail" from the urls.py page
		# also fills in kew word argument id
		#return "/posts/%s/" % (self.id)   #define url by function call to db model
	# for python 2
	#def __unicode__(self):
	#	return self.title
	class Meta: #describes model, handles anything not a field

		ordering = ["-timestamp", "-updated"]
		           #order by any piece of the model

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)