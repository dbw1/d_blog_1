from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect


from .models import Post
from .forms import PostForm
# Create your views here.

#support functions for Posts app
def validate_user(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied

# Actual views for Posts app
#request comes in send a response
def posts_create(request):
	validate_user(request)
	form = PostForm(request.POST or None, request.FILES or None) #POST request text field data, FILES requests files
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

def posts_detail(request, slug): #retrieve
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, slug=slug)
	context = {
		"title": instance.title,
		"instance":instance
	}
	return render(request, 'post_detail.html', context)

def posts_list(request): #list items
	queryset_list = Post.objects.all() #all queries
	queries_per_page_var = 5
	paginator = Paginator(queryset_list, queries_per_page_var) # Show 25 contacts per page
	page_request_var = 'page' #change page search name (see post_list.html)
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page) #queries in a given paginator set
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,  #add queryset to post list we can see
		"title": "List",
		"page_request_var": page_request_var
	}

	return render(request, 'post_list.html', context)




def posts_update(request, slug):
	validate_user(request)
	instance = get_object_or_404(Post, slug = slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance) #checks for validation redirects what you had
	if form.is_valid():   #saves the form data into database if valid
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,  #renders existing id's title
		"instance":instance,      #renders existing id's content
		"form": form,             #renders actual form information
	}
	return render(request, 'post_form.html', context)

def posts_delete(request, id):
	validate_user(request)
	instance = get_object_or_404(Post, id = id)
	instance.delete()
	messages.success(request, "Succesfully deleted")
	return redirect("posts:list")