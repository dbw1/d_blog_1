from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm
# Create your views here.

#request comes in send a response
def posts_create(request):
	form = PostForm(request.POST or None) #checks for validation errors through Form function
	if form.is_valid():   #saves the form data into database if valid
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Post Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	# Below commented method would print out title or content and then we could save
	# to model db, however this doesn't validate data, so it is inferior to above Posts method used
	# if request.method == 'POST':
	# 	print (request.POST.get("content"))
	# 	print (request.POST.get("title")
	context = {
		"form": form,
	}
	return render(request, 'post_form.html', context)

def posts_detail(request, id): #retrieve
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id = id)
	context = {
		"title": instance.title,
		"instance":instance
	}
	return render(request, 'post_detail.html', context)

def posts_list(request): #list items
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,  #add queryset to post list we can see
		"title": "list"
	}
	return render(request, 'post_list.html', context)

def posts_update(request, id):
	instance = get_object_or_404(Post, id = id)
	form = PostForm(request.POST or None, instance=instance) #checks for validation redirects what you had
	if form.is_valid():   #saves the form data into database if valid
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Update Successful")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,  #renders exiting id's title
		"instance":instance,      #renders exiting id's content
		"form": form,             #renders actual form information
	}
	return render(request, 'post_form.html', context)

def posts_delete(request, id):
	instance = get_object_or_404(Post, id = id)
	instance.delete()
	messages.success(request, "Succesfully deleted")
	return redirect("posts:list")