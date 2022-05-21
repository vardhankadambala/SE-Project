from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User1(models.Model):
	user=models.CharField(max_length=100,null=True)
	phone = models.CharField(max_length=100,null=True)
	address = models.CharField(max_length=100,null=True)
	
	def __str__(self):
		return self.phone

class menu(models.Model):
	fname=models.CharField(max_length=100,null=True)
	ftype = models.CharField(max_length=100,null=True)
	cost = models.CharField(max_length=100,null=True)
	
	def __str__(self):
		return self.fname

class cust(models.Model):
	cname=models.CharField(max_length=100,null=True)
	cphone = models.CharField(max_length=100,null=True)
	caddress = models.CharField(max_length=100,null=True)
	ctype = models.CharField(max_length=100,null=True)
	camount = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.name

class cust1(models.Model):
	cname=models.CharField(max_length=100,null=True)
	cphone = models.CharField(max_length=100,null=True)
	caddress = models.CharField(max_length=100,null=True)
	ctype = models.CharField(max_length=100,null=True)
	camount = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.cname