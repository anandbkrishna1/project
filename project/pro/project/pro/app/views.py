from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        if request.method=='POST':
            username=request.POST.get('user_name')
            email= request.POST.get('email')
            pwd = request.POST.get('pwd')
            cnfpwd = request.POST.get('cnfpwd')
            if pwd==cnfpwd:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username Already Exist")
                    return redirect('/register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Already Exist")
                    return redirect('/register')
                else:
                    user=User.objects.create(username=username,email=email,password=pwd)
                    user.save()
                return redirect('/')
            else:
                messages.info(request, "Password Not Match")
                return redirect('/register')
    return render(request,'signup.html')