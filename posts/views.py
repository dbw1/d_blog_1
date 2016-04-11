from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

#request comes in send a response
def posts_create(request):
	return HttpResponse("<h1>Hello</h1>")  #must wrap function into a url

def posts_detail(request, id=None): #retrieve
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id = 11)
	context = {
		"title": "detail",
		"instance":instance
	}
	return render(request, 'post_detail.html', context)

def posts_list(request): #list items
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,  #add queryset to post list we can see
		"title": "list"
	}
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My User list"
	# 	}
	# else:
	# 	context = {
	# 		"title": "No page for you!"
	# 	}
	return render(request, 'index.html', context)

def posts_update(request):
	return HttpResponse("<h1>update</h1>")

def posts_delete(request):
	return HttpResponse("<h1>delete</h1>")