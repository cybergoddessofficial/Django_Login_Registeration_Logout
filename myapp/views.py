from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def Index(request):
	name='User'
	return render(request,"index.html",{'name':name})

def register(request):
	if request.method=="POST":
		first_name=request.POST.get("first_name")
		# fname=request.POST['first-name']
		last_name=request.POST.get("last_name")
		username=request.POST.get("username")
		email=request.POST.get("email")
		password=request.POST.get("password")
		password2=request.POST.get("password2")
		if password==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"username already taken")
				return redirect(register)
			elif User.objects.filter(email=email).exists():
				messages.info(request,"email already taken")
				return redirect(register)
			else:
				user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
				user.save()
				print("user created")
				return redirect(login)
		else:
			messages.info(request,"password mismatched")
			print("invalid password")
			return redirect(register)
	return render(request,"register.html")

def login(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect(userindex)
		else:
			messages.info(request,"invalid credentials")
			return redirect(login)
	return render(request,"login.html")

def userindex(request):
	return render(request,"usersite/userindex.html")

def logout(request):
	auth.logout(request)
	return redirect(Index)