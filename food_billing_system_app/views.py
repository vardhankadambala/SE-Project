from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from food_billing_system import settings
from PIL import Image,ImageDraw,ImageFont
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def index(request):
	return render(request,"index.html")

def index1(request):
	return render(request,"index1.html")

def login(request):
	if request.method=="POST":
		uname1=request.POST["uname"]
		password1=request.POST["pswd"]

		user = auth.authenticate(username=uname1,password=password1)
		print(user)
		if user:
			auth.login(request, user)
			return redirect("owner")
		else:
			messages.info(request,"Invalid Username or Password")
			return redirect("error")
	return render(request,"login.html")

def login1(request):
	if request.method=="POST":
		uname1=request.POST["uname"]
		password1=request.POST["pswd"]

		user = auth.authenticate(username=uname1,password=password1)
		print(user)
		if user:
			auth.login(request, user)
			return redirect("employee")
		else:
			messages.info(request,"Invalid Username or Password")
			return redirect("error1")

	return render(request,"login1.html")

def login_2(request):
	return render(request,"login_2.html")

def login_3(request):
	return render(request,"login_3.html")

def error(request):
	return render(request,"error.html")

def error1(request):
	return render(request,"error1.html")

def change(request):
	if request.method == "POST":
		fm=PasswordChangeForm(user=request.user, data=request.POST)
		if fm.is_valid():
			fm.save() 
			return redirect("index")
	else:
		fm = PasswordChangeForm(user=request.user)
	return render(request,"change.html",{'form':fm})

def change1(request):
	return render(request,"change1.html")

def signup(request):
	form = UserReg(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("login_2")
	return render(request,"signup.html",{"form":form})

def signup1(request):
	form = UserReg1(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("login_3")
	return render(request,"signup1.html",{"form":form})

def owner(request):
	return render(request,"owner.html")

def employee(request):
	return render(request,"employee.html")

def calc(request):
	return render(request,"calc.html")

def empman(request):
	data=User.objects.all()
	return render(request,"empman.html",{"data":data})

def fill(request):
	if request.method=="POST":
		user1=request.POST["uname"]
		phone1=request.POST["pnum"]
		add=request.POST["add"]

		data_db_table = User1( user= user1,phone= phone1,address= add,)
		data_db_table.save()

		data = {"user":user1,"phone":phone1,"address":add}
		
		return render(request,"empdet.html")
	return render(request,"fill.html")

def fill1(request):
	if request.method=="POST":
		user1=request.POST["uname"]
		phone1=request.POST["pnum"]
		add=request.POST["add"]

		data_db_table = User1( user= user1,phone= phone1,address= add,)
		data_db_table.save()

		data = {"user":user1,"phone":phone1,"address":add}
		
		return render(request,"empdet.html")
	return render(request,"fill1.html")

def menuadd(request):
	if request.method=="POST":
		fname1=request.POST["name"]
		ftype1=request.POST["ftype"]
		fcost1=request.POST["cost"]

		data_db_table = menu( fname= fname1,ftype= ftype1,cost=fcost1)
		data_db_table.save()

		data = {"fname":fname1,"ftype":ftype1,"cost":fcost1}
		return render(request,"confirm.html")
	return render(request,"menuadd.html")

def menuadd1(request):
	if request.method=="POST":
		fname1=request.POST["name"]
		ftype1=request.POST["ftype"]
		fcost1=request.POST["cost"]

		data_db_table = menu( fname= fname1,ftype= ftype1,cost=fcost1)
		data_db_table.save()

		data = {"fname":fname1,"ftype":ftype1,"cost":fcost1}
		return render(request,"confirm1.html")
	return render(request,"menuadd1.html")

def cust(request):
	if request.method=="POST":
		cname1=request.POST["name"]
		cnum1=request.POST["num"]
		cadd1=request.POST["add"]
		ctype1=request.POST["type"]
		camount1=request.POST["amount"]
		data_db_table = cust1( cname= cname1,cphone=cnum1,caddress=cadd1,ctype= ctype1,camount=camount1)
		data_db_table.save()
		return render(request,"confirm2.html")
	return render(request,"cust.html")



def profile(request):
	return render(request,"profile.html")

def empdet(request):
	data = User1.objects.all() 
	return render(request,"empdet.html",{"data":data})

def empdet1(request):
	data1=User.objects.all()
	data = User1.objects.all() 
	data2= User1.objects.filter(user=request.user)
	return render(request,"empdet1.html",{"data":data2})

def delete(request,Id):
	data=User.objects.get(id=Id)
	data.delete()
	return redirect("empman")

def delete1(request,Id):
	data=menu.objects.get(id=Id)
	data.delete()
	return redirect("menudis")

def delete2(request,Id):
	data=User1.objects.get(id=Id)
	data.delete()
	return redirect("empdet")

def delete3(request,Id):
	data=cust1.objects.get(id=Id)
	data.delete()
	return redirect("cust1")

def menudis(request):
	data=menu.objects.all()
	return render(request,"menudis.html",{"data":data})

def cust11(request):
	data=cust1.objects.all()
	return render(request,"cust1.html",{"data":data})

def netbank(request):
	return render(request,"netbank.html")

def cre_deb(request):
	return render(request,"cre_deb.html")

def payment(request):
	return render(request,"payment.html")

def sucess(request):
	return render(request,"sucess.html")

def netbank1(request):
	return render(request,"netbank1.html")

def cre_deb1(request):
	return render(request,"cre_deb1.html")

def payment1(request):
	return render(request,"payment1.html")

def sucess1(request):
	return render(request,"sucess1.html")

def about(request):
	return render(request,"about.html")

def contact(request):
	return render(request,"contact.html")