from django.shortcuts import render,redirect
from .models import User,Students
from django.http import JsonResponse



# Create your views here.

def login(request):
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
			return redirect("/home/")
		else:
			return render(request, 'login.html', {'status': 1})
	else:
		return render(request, 'login.html', {'status' : 1})


def lc(request):
	obj = Students.objects.filter(enrollment = request.POST['enrollment'])
	if not obj:
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
		last_student = Students.objects.all().order_by('-id').first()
		if last_student:
			student.serial_no = int(last_student.serial_no) + 1
		else:
			student.serial_no = 1
		student.save()
	else:
		return JsonResponse({'state': 1})
	return JsonResponse({'state': 0})


def genlc(request):
	student = Students.objects.filter(enrollment = request.POST['enrollment'])
	if student:
		return render(request, 'lc.html', {'row' : student[0]})
	else:
		return render(request, 'enroll.html', {'state': 1})

def adddata(request):
	return render(request, 'index.html')

def enroll(request):
	return render(request, 'enroll.html', {'link': '/genlc/', 'btn_name': 'Show LC'})



def showUpdate(request):
	return render(request, 'enroll.html', {'link': '/update/', 'btn_name': 'Update LC'})

def showDelete(request):
	return render(request, 'enroll.html', {'link': '/delete/', 'btn_name': 'Delete LC'})

def showLc(request):
	last_student = Students.objects.all().order_by('-id').first()
	return render(request, 'lc.html', {'row' : last_student})

def update(request):
	student = Students.objects.filter(enrollment = request.POST['enrollment'])
	if student:
		return render(request, 'update.html', {'row' : student[0]})
	else:
		return render(request, 'enroll.html', {'status' : 1})


def delete(request):
	student = Students.objects.filter(enrollment = request.POST['enrollment'])
	if student:
		student[0].delete()
		return render(request, 'enroll.html', {'link': '/delete/', 'btn_name': 'Delete LC', 'state': 5})
	else:
		return render(request, 'enroll.html', {'link': '/delete/', 'btn_name': 'Delete LC', 'state': 1})

def home(request):
	return render(request, 'home.html')