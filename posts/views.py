from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#request comes in send a response
def posts_create(request):
	return HttpResponse("<h1>Hello</h1>")  #must wrap function into a url

def posts_detail(request): #retrieve
	context = {
		"title": "detail"
	}
	return render(request, 'index.html', context)

def posts_list(request): #list items
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