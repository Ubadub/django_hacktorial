from django.http import HttpResponse
from django.shortcuts import render

from blogpost.models import Post

# def homepage(request):
# 	return HttpResponse("Hello World")

# def homepage(request):
# 	return HttpResponse("<html><body><p>Hello World</p></body></html>")

def homepage(request):
	return render(request, 'homepage.html', {'blog_posts' : Post.objects.all()})