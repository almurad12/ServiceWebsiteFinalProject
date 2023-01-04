
# Create your views here.
from django.shortcuts import render,HttpResponseRedirect,redirect
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# def adminlogin(request):
#     try:
#         if request.user.is_authenticated:
#             return redirect('/')
#         if request.method =="POST":
#            username = request.POST.get("username")
#            password = request.POST.get("password")
#            user_obj = User.objects.filter(username=username)
#            if not user_obj.exists():
#                 messages.info(request,'Account not found')
#                 return HttpResponseRedirect(request.META.get(HTTP_REFERER))
#             user_obj = authenticate(username=username,password=password)
#             if user_obj and user_obj.is_superuser:
#                 login(request,user_obj)
#                 return redirect('/')
#             messages.info(request,'Invalid password')
#             return redirect('/')
#         return redirect('/')
#     return render(request,'adminLogin.html')
# except Exception as e:
#     print(e)

    # return redirect('')

def newadminpanel(request):
    return render(request,'adminpanel/cartDashboard.html')

def servicelist(request):
    return render(request,'adminpanel/allservicelist.html')

def alluserlist(request):
    return render(request,'adminpanel/alluserlist.html')