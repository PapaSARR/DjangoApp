from django.db import models

class User(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=128)

	# def __init__(self,email,password):
	# 	self.email = email
	# 	self.password = password

	class Meta:
		db_table = 'users'