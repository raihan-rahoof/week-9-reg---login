from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.views.decorators.cache import never_cache 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required , user_passes_test




# Create your views here.
@never_cache
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user and user.is_superuser:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('adminlogin')
    else:
       return render(request,'adminlogin.html')


def logout_view(request):
    logout(request)
   
    return redirect('adminlogin')        

   
    

# ---------------- Read------------------------------------
# def dashboard(request):
#     u=users.objects.all()

#     context = {
#         'users':u,
#     }
#     return render(request,'custumadmin.html',context)

@never_cache
def dashboard(request):

    if request.user.is_superuser:
        
        us = User.objects.all()
        query = request.GET.get('q')  
        if query:
            us = User.objects.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query)|
                Q(last_name__icontains=query)|
                Q(email__icontains=query)
                ) 
            

        context = {
            'users': us,
            'search_query': query,  
        }
        return render(request, 'custumadmin.html', context)
    else:
        return redirect('adminlogin')


#----------------create/add----------------------------------------

def add(request):
    if request.user.is_superuser:
        if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']

        
            if User.objects.filter(username=username).exists():
                messages.info(request,'Recent Username already in use,try new one')
                return redirect('add')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Recent Email already used,try new one')
                return redirect('add')
            else:
                user=User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email
                )
                user.save()
        return redirect('dashboard')
    else:
        return redirect('adminlogin')

    

#--------------edit---------------------------------------------

def edit(request):
    u=User.objects.all()

    context = {
        'users':u,
    }
    return redirect('dashboard',context)

#-------------update data-----------------------------------------

def update(request, id):
    if request.user.is_superuser:
        if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']

            user=User(
                id=id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email
            )

            user.save()

            return redirect('dashboard')
    else:
        return redirect('adminlogin')
        

#------------delete data-----------------------------------------

def delete(request,id):
    if request.user.is_superuser:
        user=User.objects.filter(id=id)
        user.delete()
        context = {
            'users':user,
        }
        return redirect('dashboard')
    else:
        return redirect('adminlogin')    





