from django.shortcuts import render
from django.http import HttpResponse
from Demo.models import UsrReg

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def reg(request):
	if request.method == "POST":
		a = request.POST['uname']
		b = request.POST['pwd']
		c = request.POST['em']
		d = request.POST['ag']
		w = UsrReg(user_name=a,pass_word=b,email=c,age=d)
		w.save()
		return HttpResponse("User Registered Successfully")
	return render(request,'html/registration.html')



