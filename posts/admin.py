from django.contrib import admin

# Register your models here.
from .models import Post #.models is a relative callingof posts.models

class PostModelAdmin(admin.ModelAdmin):  #links post model to the post model admin
	list_display = ["__str__", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated","timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)