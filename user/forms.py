from django import forms
from user.models import User
# Create your models here.

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'
		widgets = {
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class' : 'form-control'})
		}