from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("<h1 style='color:green;background-color:yellow'>Hi Welcome to APSSDC Workshop</h1>")
def home1(req):
	return HttpResponse("<h2>Hi</h2><script>alert('hi Students')</script>")

def names(req,name):
	return HttpResponse("my name is "+name)

def tags(req):
	return render(req,'webseries/tag.html')

def colortags(req):
	return render(req,'webseries/color.html')

def re(request):
	if request.method == "POST":
		a = request.POST['fname']
		b = request.POST['mk']
		return render(request,'webseries/viewdata.html',{'f':a,'t':b})
	return render(request,'webseries/registration.html')

