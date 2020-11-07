from user.forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render

def connexion(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            login(user)
            return redirect('/view')
    else:
        form = UserForm() 
    return render(request, 'index.html', {'form': form}) 