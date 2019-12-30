from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

from .models import BlogPost
from .forms import BlogPostModelForm

# fetch the data from database and render

def blog_post_list_view(request):
	qs = BlogPost.objects.all()
	template_name = "blog_post_list_view.html"
	context = {'object_list': qs}
	return render(request,template_name,context)
@login_required
@staff_member_required
def blog_post_create_view(request):
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = BlogPostModelForm()
	template_name = "form.html"
	context = {'form': form}
	return render(request,template_name,context)

def blog_post_retrieve_view(request, slug):
	obj = get_object_or_404(BlogPost,slug = slug)
	template_name = "blogpost_details.html"
	context = {'object': obj}
	return render(request,template_name,context)

def blog_post_update_view(request,slug):
	obj = get_object_or_404(BlogPost,slug = slug)
	form = BlogPostModelForm(request.POST or None)
	template_name = "form.html"
	context = {'form': None, 'title':f"Update {obj.title}"}
	return render(request,template_name,context)

def blog_post_delete_view(request,slug):
	obj = get_object_or_404(BlogPost,slug = slug)
	template_name = "blog_post_delete.html"
	context = {'object': obj}
	return render(request,template_name,context)
