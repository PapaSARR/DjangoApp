from django import forms
from user.models import User
# Create your models here.

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = '__all__'