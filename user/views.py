from user.forms import UserForm
from user.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

def connexion(request):
	context={}
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = make_password(form.cleaned_data['password'])
			user = User.objects.filter(email=email)
			if not user.exists():
				User.objects.create(email=email,password=password)
				user = User.objects.get(email=email)
				context = {'id': user.id, 'email': user.email, 'form':form}
			else:
				context = {'id': user[0].id, 'email': user[0].email, 'form':form}
		return render(request,'edition.html', context)
	else:
		form = UserForm() 
	return render(request, 'connexion.html',  {'form':form})


def edition(request,id):
	user = User.objects.get(id=id)
	form = UserForm(instance=user)
	if request.method == "POST":
		form = UserForm(request.POST,instance=user)
		if form.is_valid():
			#form.save()
			User.objects.filter(id=user.id).update(email=user.email)
		context = {'id': user.id, 'email': user.email, 'form':form}
		return render(request,'edition.html', context)
	
	