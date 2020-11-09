from user.forms import UserForm
from user.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

def connexion(request):
	if request.method == "POST":
		return redirect('edition')
	else:
		form = UserForm() 
	return render(request, 'connexion.html',  {'form':form})


def edition(request):
	context={}
	form = UserForm(request.POST)
	if form.is_valid():
		email = form.cleaned_data['email']
		password = make_password(form.cleaned_data['password'])
		user = User.objects.filter(email=email)
		if not user.exists():
			User.objects.create(email=email,password=password)
			user = User.objects.get(email=email)
			context = {'email': user.email, 'form':form}
		else:
			context = {'email': user[0].email,  'form':form}
	return render(request,'edition.html', context)