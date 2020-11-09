from user.forms import UserForm
from user.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

def connexion(request):
	context = {}
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = make_password(form.cleaned_data['password'])
			user = User.objects.filter(email=email)
		if not user.exists():
			User.objects.create(email=email,password=password)
			user = User.objects.get(email=email)
			context = {'user_id':user.id,'user_email':user.email}
		else:
			context = {'user_id':user[0].id,'user_email':user[0].email}     
		return render(request, 'accueil.html', context)	
	else:
		form = UserForm()
		context['form'] = form 
	return render(request, 'connexion.html', context) 

def edition(request, user_id):
	return render(request, 'edition.html', user_id)