from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views	
from django.core.mail import send_mail
from django_otp.oath import totp
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
from myparliament.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import sweetify
# from .models import Application
from myparliament.models import Application
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")





def emailotpverify(request):
	if request.method == 'GET':
		return render(request, 'register1.html',{ 'email'  : None } )
	if request.method == 'POST':
		try:
			isverified = request.POST.get('isverified')
			email = request.POST.get('email')
			print(isverified,email)
			if isverified == 'True' :
				print("okk")
				try:
					return render(request, 'register2.html',{'email':email,'isverified':isverified})
				except:
					print("Err")
			elif isverified is None:
				# print("passed")
				pass		
				# return render(request, 'register2.html',  {'email':email})
				# return HttpResponse("nextpage")
		except:
			pass	

		try:
			# print("reaach")
			email = request.POST.get('email')
			print(email)
			try:
				match = User.objects.filter(username = email).count()
				print(match)
				if match ==0:	
					print(email)
					secret_key = b'1234567890123467890'
					otp = totp(key=secret_key, step=1, digits=6, t0= 1)
					send_mail(
					    'Otp confirmation for My parliament',
					    'Your otp is : ' + str(otp),
					    settings.EMAIL_HOST_USER,
					    [ email ],
					    fail_silently=False,
					)

					return render(request, 'register1.html',  {'email':email, 'otp' : otp})
				
				
			except Exception as e:
				print(e)
				# sweetify.error(request, "err", persistent=':(')
			return render(request, 'register1.html')	
		except Exception as e:
			print(e)
			return HttpResponse("Error")	
# def verify(request):
# 	if request.method == 'POST':
def register(request):
	

	if request.method =='POST':
		form = RegistrationForm(request.POST)
		logout(request)
		if form.is_valid():
			form.save()
			new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
			login(request,new_user)
			return render(request,'application.html')
		else:
			# print(form)
			email= form.cleaned_data.get("email")
			return render(request, 'register2.html', {'form': form,'email':email})
        # if form.is_valid():
        # 	form.save()
        # 	return redirect(reverse('/'))
	    # else:
	    #     form = RegistrationForm()

	    #     args = {'form': form}
	    #     return render(request, 'accounts/reg_form.html', args)


# @login_required
# def application(request):
# 	if request.method == 'GET' :
# 		print("GETtttt")
# 		user = User.objects.get(username  = request.user.email)
# 		data = Application.objects.filter(email1 = user).count()
# 		if data != 0:
# 			data = list(Application.objects.filter(email1 = user).values())
# 			# print(list(data))
# 			return render(request, 'application.html',{'data' : data })
# 	return render(request, 'application.html',{'data' : None })

# 	if request.method == 'POST':
# 		print("POSRRR")
# 		user = User.objects.get(username  = request.user.email)
# 		email= request.user.email
# 		phnno=	request.POST.get('phnno')
# 		gender = request.POST.get('gender')
# 		fulladdd = request.POST.get('fulladdd')
# 		city = request.POST.get('city') 
# 		state=request.POST.get('state')
# 		LOE = request.POST.get('education')
# 		FOS = request.POST.get('FOS')
# 		Institute = request.POST.get('institute')
# 		try:
# 			# print("onr")
# 			print(str(email), phnno , fulladdd , LOE, gender, city, state)
# 			try:
# 				num_results = Application.objects.filter(email1 = user).count()

# 				print(num_results)
# 			except Exception as e:
# 				print(type(e))	
			
# 			if num_results == 0 :
# 				print ("okkkkk")
# 				a=Application(email1 = user,phnno = phnno , gender = gender , fulladdd = fulladdd , city = city , state = state , LOE= LOE , FOS = FOS , Institute = Institute )
# 				a.save()
# 			else:
# 				try:
# 						t=Application.objects.get(email1 = user)
							
# 						# t.email1 = email
# 						t.phnno = phnno
# 						t.gender =gender
# 						t.fulladdd = fulladdd
# 						t.city =city
# 						t.state = state
# 						t.LOE = LOE
# 						t.FOS = FOS 
# 						t.Institute = Institute
# 						t.save()
# 				except Exception as e:
# 						print (e)
# 			return HttpResponse("done")			
# 		except:
# 				return HttpResponse("err")		


@login_required
def application1(request):
	if request.method == 'GET' :
		print("GETtttt")
		user = User.objects.get(username  = request.user.email)
		data = Application.objects.filter(email1 = user).count()
		if data != 0:
			data = list(Application.objects.filter(email1 = user).values())
			# print(list(data))
			return render(request, 'application.html',{'data' : data })
		return render(request, 'application.html')	

	if request.method == 'POST' :
		
		print("POSRRR")
		user = User.objects.get(username  = request.user.email)
		email= request.user.email
		phnno=	request.POST.get('phnno')
		gender = request.POST.get('gender')
		fulladdd = request.POST.get('fulladdd')
		city = request.POST.get('city') 
		state=request.POST.get('state')
		LOE = request.POST.get('education')
		FOS = request.POST.get('FOS')
		Institute = request.POST.get('institute')
		try:
			# print("onr")
			print(str(email), phnno , fulladdd , LOE, gender, city, state)
			try:
				num_results = Application.objects.filter(email1 = user).count()

				print(num_results)
			except Exception as e:
				print(type(e))	
			
			if num_results == 0 :
				print ("okkkkk")
				a=Application(email1 = user,phnno = phnno , gender = gender , fulladdd = fulladdd , city = city , state = state , LOE= LOE , FOS = FOS , Institute = Institute )
				a.save()
			else:
				try:
						t=Application.objects.get(email1 = user)
							
						# t.email1 = email
						t.phnno = phnno
						t.gender =gender
						t.fulladdd = fulladdd
						t.city =city
						t.state = state
						t.LOE = LOE
						t.FOS = FOS 
						t.Institute = Institute
						t.save()
				except Exception as e:
						print (e)
			return HttpResponse("done")			
		except:
				return HttpResponse("err")						

@login_required
def application2(request):
	if request.method == 'GET':
		user = User.objects.get(username  = request.user.email)
		data = Application.objects.filter(email1 = user).count()
		if data != 0:
			data = list(Application.objects.filter(email1 = user).values())
			# print(list(data))
			
			return render(request, 'application2.html',{'data' : data })
		return redirect('myparliament/application1')
	if request.method == 'POST':
		user = User.objects.get(username  = request.user.email)
		que1=	request.POST.get('que1')
		que2 = request.POST.get('que2')
		que3 = request.POST.get('que3')
		t=Application.objects.get(email1 = user)
		t.que1=que1
		t.que2=que2
		t.que3=que3
		t.save()
		return HttpResponse("donn")
@login_required
def application3(request):
	if request.method == 'GET':
		user = User.objects.get(username  = request.user.email)
		data = Application.objects.filter(email1 = user).count()
		if data != 0:
			data = list(Application.objects.filter(email1 = user).values())
			# print(list(data))
			
			return render(request, 'application3.html',{'data' : data })
		return redirect('myparliament/application1')
	if request.method == 'POST':
		user = User.objects.get(username  = request.user.email)
		que4=	request.POST.get('que4')
		que5 = request.POST.get('que5')
		que6 = request.POST.get('que6')
		que7 = request.POST.get('que7')
		t=Application.objects.get(email1 = user)
		t.que4=que4
		t.que5=que5
		t.que6=que6
		t.que7 = que7
		t.save()
		return HttpResponse("donn")		
@login_required
def application4(request):
	if request.method == 'GET':
		user = User.objects.get(username  = request.user.email)
		data = Application.objects.filter(email1 = user).count()
		if data != 0:
			data = list(Application.objects.filter(email1 = user).values())
			# print(list(data))
			
			return render(request, 'application4.html',{'data' : data })
		return redirect('myparliament/application1')
	if request.method == 'POST':
		user = User.objects.get(username  = request.user.email)
		que8=	request.POST.get('que8')
		que9 = request.POST.get('que9')
		
		t=Application.objects.get(email1 = user)
		t.que8=que8
		t.que9=que9
		
		t.save()
		return HttpResponse("donn")									

@login_required
def application5(request):
	if request.method == 'GET':
		user = User.objects.get(username  = request.user.email)
		data = Application.objects.filter(email1 = user).count()
		if data != 0:
			data = list(Application.objects.filter(email1 = user).values())
			# print(list(data))
			
			return render(request, 'application5.html',{'data' : data })
		return redirect('myparliament/application1')
