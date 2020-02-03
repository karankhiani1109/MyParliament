from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Application(models.Model):
	email1 = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
	phnno = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	fulladdd = models.CharField(max_length=100)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	LOE = models.CharField(max_length=20)
	FOS = models.CharField(max_length=20)
	Institute = models.CharField(max_length=50) 
	que1 = models.CharField(max_length = 50,default = "")
	que2= models.CharField(max_length= 1000 ,default = "" ,null= True)
	que3 = models.CharField(max_length = 1000,default = ""	,null= True)
	is_step2_completed = models.BooleanField(default = False)
	que4 = models.CharField(max_length = 50,default = "")
	que5= models.CharField(max_length= 100 ,default = "")
	que6 = models.CharField(max_length = 1000,default = "", null= True	)
	que7 = models.CharField(max_length = 1000,default = "",	null= True )
	is_step3_completed = models.BooleanField(default = False)
	que8 = models.CharField(max_length = 1000,default = "",	null= True )
	que9 = models.CharField(max_length = 1000,default = "",	null= True )
	is_step4_completed = models.BooleanField(default = False)




