from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Profile
def page1(request):
    if request.method=="POST":
        uname=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email=request.POST['email']
        ph_no=request.POST['ph_no']
        password1=request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username Taken')
                return redirect('page1')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('page1')
            else:
                user = User.objects.create_user(username=uname, password=password1, email=email,
                                                first_name=fname, last_name=lname)
                user.save()
                profile=Profile(user=user,ph_no=ph_no)
                profile.save()
                messages.info(request,"User created")
                return redirect('page2')
        else:
            messages.info(request, 'password not matching.....')
            return redirect('page1')
    else:
        return render(request, 'Page1.html')

def page2(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,"Page3.html")
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('page2')
    else:
        return render(request,'Page2.html')
def logout(request):
    auth.logout(request)
    messages.info(request,"Logged Out Successfully")
    return redirect('page1')
# Create your views here.
