from logging import error

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import random

def register(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully')  
            return redirect('login')  
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:  
        form = CustomUserCreationForm()
    
    context = {  
        'form': form  
    }  
    return render(request, 'dsacounter/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'bot/login.html', {'form': form})

@login_required
def home(request):
    form1 = ResultForm()
    form2 = joinclass()
    if request.method == 'POST':
        form = ResultForm(request.POST)
        
        if form.is_valid():
            ti=form.cleaned_data.get('takentime')
            if not ti=="00:00:00" :
                form.save()
                return redirect('home')
            else:
                messages.error(request, 'start timer')
                return redirect('home')
        else:
            print("Form is invalid:", form.errors)
    if request.method == 'POST':
        form = joinclass(request.POST)

        if form.is_valid():
            val=form.cleaned_data.get('student')
            val2=form.cleaned_data.get('room')
            obj1=studying.objects.filter(student=val,room=val2)
            if not obj1.exists():
                form.save()
                messages.success(request, 'joined class successfully!')
                return redirect('home')
            else:
                messages.error(request, "Already in that class")
                return redirect('home')  # Redirect to the home page or a success page
        else:
            messages.error(request, "invalid class id")
            return redirect('home')
    return render(request, 'dsacounter/counter.html', {'form1': form1, 'form2': form2})

def logout_view(request):
    logout(request)
    return redirect('reg')

@login_required
def results(request,username):
    obj=progress.objects.filter(username=username)[::-1]
    return render(request, 'dsacounter/results.html', { 'obj' : obj} )
@login_required
def dele(request ,date , submittime, username):
    obj=get_object_or_404(progress,date=date, submittime=submittime)
    obj.delete()
    return redirect('results',username=username)
def teacherlogin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                te = teacher.objects.filter(teacher=user)
                if not te.exists():
                    messages.error(request, "Become a teacher first")
                    return redirect('tlogin')
                else:
                    login(request, user)
                    return redirect('dashboard')
            else:
                messages.error(request, 'Please correct the error(s) below.')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'dsacounter/tlogin.html', context)
@login_required(login_url='teacherlogin')
def dashboard(request):
    username = request.user
    tea = teacher.objects.filter(teacher=username).first()
    if tea is not None:
        obj = rooms.objects.filter(teacherid=username)  # Assuming `rooms` is your model
        def generate_unique_number():
            while True:
                random_number = random.randint(10000, 99999)
                if not obj.filter(roomid=random_number).exists():
                    return random_number
        unique_number = generate_unique_number()
        if request.method=='POST':
            form=room(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        form = room()
        return render(request, 'dsacounter/dashboard.html',{ 'obj': obj , 'unique_number': unique_number,'form':form })
    else:
        return redirect('tlogin')
@login_required(login_url='teacherlogin')
def roomdelete(request, roomid):
    username = request.user
    tea = teacher.objects.filter(teacher=username).first()
    if tea is not None:
        obj=get_object_or_404(rooms,roomid=roomid)
        obj.delete()
    else:
        return redirect('tlogin')

@login_required(login_url='teacherlogin')
def myclass(request, userid):
    obj1 = get_object_or_404(User, id=userid)
    obj2 = rooms.objects.filter(students=userid)
    return render(request, 'dsacounter/myclasses.html', {'obj1': obj1, 'obj2': obj2})
@login_required(login_url='teacherlogin')
def submissions(request, roomid):
    username = request.user
    tea = teacher.objects.filter(teacher=username).first()
    if tea is not None:
        obj1= rooms.objects.get(roomid=roomid)
        obj=obj1.students.all()
        obj2=progress.objects.filter(username__in=obj)
        return render(request, 'dsacounter/submissions.html', {'class': obj1, 'obj2': obj2})
    else:
        return redirect('tlogin')
@login_required(login_url='teacherlogin')
def deletestudent(request, roomid, studentid):
    username = request.user
    tea = teacher.objects.filter(teacher=username).first()
    if tea is not None:
        obj=get_object_or_404(studying,room=roomid,student=studentid)
        obj.delete()
        messages.success(request, 'Deleted suceesfully')
        return redirect('dashboard')
    else:
        return redirect('tlogin')
@login_required(login_url='login')
def exitclass(request, userid, roomid):
    obj = get_object_or_404(studying, room=roomid, student=userid)
    obj.delete()
    messages.success(request, 'Exited suceesfully')
    return redirect('myclass', userid)

def tsignup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            messages.error(request,"User does not exist first create a account")
            return redirect('tsignup')
        else:
            users=authenticate(username=username,password=password)
            if users is None:
                messages.error(request,'Incorrect password')
                return redirect('tsignup')
            else:
                te=teacher.objects.filter(teacher=user)
                if not te.exists():
                    newt=teacher.objects.create(teacher=user)
                    newt.save()
                    return redirect('tlogin')
                else:
                    messages.error(request,'Already a teacher')
    return render(request,'dsacounter/tsignup.html')
