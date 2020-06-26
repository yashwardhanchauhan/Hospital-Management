from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        user_type=request.POST['type']
        if User.objects.filter(username=username).exists()==False:
            if pwd1==pwd2:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=pwd1)
                user.save()
                messages.info(request,"User Created")
                return redirect('/')
            else:
                messages.info(request,"Password not Matched")
                return redirect('/')
        else:
            messages.info(request,"User name Already taken")
            return redirect('/')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')