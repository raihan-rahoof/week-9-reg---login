from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.views.decorators.cache import never_cache



# Create your views here.
@never_cache
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        
        if username.strip()=='' or password.strip()=='':
            messages.info(request,'Fields should not be empty')
            return redirect(signin)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('signin')
    else: 
        return render(request,'login.html')
    


def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password2']

        if first_name.strip() == '' or last_name.strip() == ''or username.strip() == ''  or password1.strip() == '' or password2.strip() == '' or email.strip() == '':
            messages.info(request,'fieild should not be empty')
            return redirect('register') 

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            
            elif len(username) > 10 :
                messages.info(request,'Username must be less then 10 characters')
                return redirect('register')
            
            elif not username.isalnum():
                messages.info(request,'Username must be alphanumeric')
                return redirect('register')

            
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('signin')
        else:
            messages.info(request,'Password dont match')
            return redirect('register')

    else:
        return render(request,'register.html')


def signout(request):
    auth.logout(request)
    return redirect('signin')