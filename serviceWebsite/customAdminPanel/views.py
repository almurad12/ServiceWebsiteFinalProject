
# Create your views here.
from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from account.models import User
from cartanother.models import Cartanothernew
from cartanother.models import Ordernew
from service.models import Sheba
from .forms import UserForm


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
    # context ={}
    # form = UserForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    # context['form']= form
    return render(request,'adminpanel/cartDashboard.html')
    #  return render(request,'adminpanel/cartDashboard.html')

def userlist(request):
    context ={}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    context['alluserlist']= User.objects.all()
    return render(request,'adminpanel/alluserlist.html',context)

def userlistdelete(request,id):
    if request.method =='POST':
          user =User.objects.get(pk=id)
          print(user)
          user.delete()

    # context ={}
    # obj = get_object_or_404(User, id = id)
    # if request.method =="POST":
            # delete object
            # obj.delete()
            # after deleting redirect to
            # home page
            # context['alluserlist']= User.objects.all()
    return HttpResponseRedirect('/customadmin/servicelist')
    #         return HttpResponseRedirect("/")
    # return render(request, "adminpanel/allservicelist.html", context)

# def orderlist(request):
#     return render(request,'adminpanel/alluserlist.html')

##all servicelist
def servicelist(request):
    context={}
    context['allservicelist']=Sheba.objects.all()
    return render(request,'adminpanel/allservicelist.html',context)

def servicelistdelete(request):
    if request.method=='GET':
        id = request.GET.get('id')
        serviceid = Sheba.objects.get(id=id)
        print(serviceid)
        serviceid.delete()
        return HttpResponseRedirect('/customadmin/allservicelist')
    
def allpendingorderlist(request):
    context ={}
    context['allpendingorder']= Cartanothernew.objects.all()
    return render(request,'adminpanel/allpendingorder.html',context)

def pendingorderdelete(request):
     if request.method =='GET':
        id = request.GET.get('userid')
        print(id)
        pendingorder = Cartanothernew.objects.get(id=id)
        print(pendingorder)
        pendingorder.delete()
        return HttpResponseRedirect('/customadmin/allpendingorderlist')


###all orderlist
def allorderlist(request):
   context={}
   context['allorderlist']= Ordernew.objects.all()
   return render(request,'adminpanel/allorderlist.html',context)

def allorderdelete(request):
    if request.method =='GET':
        id = request.GET.get('orderid')
        print(id)
        pendingorder = Ordernew.objects.get(id=id)
        print(pendingorder)
        pendingorder.delete()
        return HttpResponseRedirect('/customadmin/allorderlist')

def alluserlist(request):
    return render(request,'adminpanel/alluserlist.html')