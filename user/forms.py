from django import forms
from user.models import User
# Create your models here.

class UserForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

	class Meta:
		model = User
		fields = '__all__'