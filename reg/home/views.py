from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache


@never_cache
def home(request):
     if not request.user.is_authenticated:
        return redirect('signin')
     else:
        return render(request,'index.html')