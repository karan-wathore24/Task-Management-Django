from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home.html")

def sign_up(request):
    return render(request,"sign_up.html")

def login_page(request):
    return render(request,"login_page.html")

def register(request):
    
    if request.method=="POST":
        fn=request.POST['first_name']
        ln=request.POST['last_name']

        em=request.POST['username']
        ps=request.POST['password']
        if em and ps is not None:
            u=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=ps)
            u.save()
            messages.success(request,"Registration Successfully !")
            return redirect("login_page")
        else:
            messages.warning(request,"Please fill the all feilds !")

            return redirect("sign_up")
    else:
        messages.success(request,"Failed !")

        return redirect("sign_up")

def loginsave(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
   
            return redirect("dashboard")
        else:
            return redirect("login_page")

@login_required(login_url="login_page")   
def dashboard(request):
    
    return render(request,"dashboard.html" )

    
def reset_ps(request):
    return render(request,"reset_ps.html")

def set_ps(request):
    if request.method=="POST":
        user=request.POST['username']
        old=request.POST['password']
        nw=request.POST['new_password']

        us=authenticate(username=user,password=old)

        if us:
            us.set_password(nw)
            us.save()
            messages.success(request,"password reset successfull")
            return redirect("dashboard")
        else:
            messages.warning(request,"failed to reset")
            return redirect("dashboard")

def forget_ps(request):
    return render(request,"forget_ps.html")        

def forget_valid(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']

        users = User.objects.filter(username=username, first_name=first_name).first()
        if users:
            messages.success(request, "Enter Your New Password")
            return render(request,"updateps.html",{"users":users})
        else:
            messages.error(request, "Invalid credentials")
            return redirect("forget_ps")
        

def upd_pss(request):
    if request.method=="POST":
        user_id = request.POST.get('user_id')
        news = request.POST['password']
        users = User.objects.filter(id=user_id).first()
        if users:
            users.set_password(news)
            users.save()
            messages.success(request, "Password updated successfully")
            return redirect("login_page")
        else:
            messages.error(request, "User not found")
            return redirect("forget_ps")



def user_logout(request):
    logout(request)
    return redirect("login_page")