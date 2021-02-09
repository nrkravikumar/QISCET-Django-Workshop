from django.shortcuts import render,redirect
from django.http import HttpResponse
from Demo.models import UsrReg
from django.contrib import messages
from Demo.forms import Usr

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
		# return HttpResponse("User Registered Successfully")
		messages.success(request,"User Registered Successfully")
		return redirect("/rg")
	return render(request,'html/registration.html')

def regi(request):
	if request.method == "POST":
		y = Usr(request.POST)
		if y.is_valid():
			y.save()
			return redirect('/rg')
	y = Usr()
	return render(request,'html/register.html',{'p':y})


def dashboard(request):
	return render(request,'html/dashboard.html')


