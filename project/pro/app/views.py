from django.contrib import messages, auth

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from .models import Watch
from .forms import WatchForm
from app.forms import*

# from app.form import*
# Create your views here.


def index(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'index.html',data)
def signup(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass')
        password2=request.POST.get('cpass')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists!!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup.html')

def user_login (request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(index)
        else:
            messages.info(request,'user not exists')
            print('user no exist')
            return redirect(user_login)
    return render(request,'login.html')



# def home(request):
#     return render(request,'index.html')


