from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime

def home_page(request):
	my_msg = "Hello there..."
	if request.user.is_authenticated:
		a = datetime.now()    
		if a.hour > 12 and a.hour <=16:
		    greet = "Afternoon!"
		    time = a.hour
		elif a.hour > 1 and a.hour <=12:
		    greet = "Morning!"
		    time = a.hour
		elif a.hour > 16 and a.hour <= 24:
		    greet = "Evening!"
		    time = a.hour
		context = {"message": my_msg,"greet": greet,"time":time}	
	else:
		context = {"message": my_msg + " Please login to get the updated details.", }
	return render(request,"home.html",context)


def about_page(request):
	about = "This is about ..."
	return render(request,"about.html",{"message": about})

def contact_page(request):
	return HttpResponse("<h1>This is a Django Tutorial Project contact_page</h1>")

def example_page(request):
	context = {"message":"Example"}
	template_name = "about.html"
	template_obj = get_template(template_name)
	return HttpResponse(template_obj.render(context))