from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 80)
	password = models.CharField(max_length = 50)

class Students(models.Model):
	gen_reg_no = models.CharField(max_length = 30)
	name = models.CharField(max_length = 50)
	cast = models.CharField(max_length = 50)
	subcast = models.CharField(max_length = 50)
	nationality = models.CharField(max_length = 100)
	enrollment = models.CharField(max_length = 100)
	birthplace = models.CharField(max_length = 500)
	dob = models.CharField(max_length = 50)
	lastschool = models.CharField(max_length = 400)
	progress = models.CharField(max_length = 100)
	conduct = models.CharField(max_length = 100)
	dol = models.CharField(max_length = 100)
	course = models.CharField(max_length = 300)
	reason = models.CharField(max_length = 300)
	remark = models.CharField(max_length = 100)
	place = models.CharField(max_length = 100)
	date = models.CharField(max_length = 100)
	serial_no = models.TextField(blank = True)