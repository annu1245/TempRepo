from django.shortcuts import render,redirect
from .models import User,Students
from django.http import HttpResponse
from django.http import JsonResponse



# Create your views here.

def index(request):
	return render(request, 'login.html')

def registrationform(request):
	return render(request, 'register.html')

def registered(request):
	obj = User.objects.filter(email = request.POST['email'])
	if obj:
		return JsonResponse({'status':1})
	user = User()
	user.name = request.POST['name']
	user.email = request.POST['email']
	user.password = request.POST['password']
	user.save()
	return JsonResponse({'status':0})

def loginform(request):
	return render(request, 'login.html')

def loggedin(request):
	obj = User.objects.filter(email = request.POST['email'])
	if obj:
		if obj[0].password == request.POST['password']:
			return render(request, 'enroll.html')
		else:
			return render(request, 'login.html', {'status': 1})
	else:
		return redirect('/loginform/')

def lc(request):
	student = Students()
	student.gen_reg_no = request.POST['gen-reg-no']
	student.name = request.POST['name']
	student.cast = request.POST['cast']
	student.subcast = request.POST['subcast']
	student.nationality = request.POST['nationality']
	student.enrollment = request.POST['enrollment']
	student.birthplace = request.POST['birthplace']
	student.dob = request.POST['dob']
	student.lastschool = request.POST['lastschool']
	student.progress = request.POST['progress']
	student.conduct = request.POST['conduct']
	student.dol = request.POST['dol']
	student.course = request.POST['course']
	student.reason = request.POST['reason']
	student.remark = request.POST['remark']
	student.place = request.POST['place']
	student.date = request.POST['date']
	student.save()
	obj = Students.objects.filter(enrollment = request.POST['enrollment'])
	return render(request, 'lc.html', {'row':obj})


def genlc(request):
	student = Students.objects.filter(enrollment = request.POST['enrollment'])
	return render(request, 'lc.html', {'row' : student})