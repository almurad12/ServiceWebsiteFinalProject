from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,redirect
from account.models import User
from service.models import Sheba
from cart.models import Cart
from cartanother.models import Cartanother,Order,Ordernew,Cartanothernew
from django.http import JsonResponse
# Create your views here.


def add_to_cart(request):
    if request.method =='GET':
        # usr = User.objects.get(id=request.user.id)
        service_id =Sheba.objects.get(id=request.GET['serviceid'])
        user_id =User.objects.get(id=request.GET['userid'])
        ###another way
        servicetitle = request.GET.get('servicetitle') 
        serviceprice = request.GET.get('serviceprice')
        serviceuseridnum = request.GET.get('serviceuseridnum')
        # service_title = Sheba.objects.get(servicetitle=request.GET['servicetitle'])
        # service_price = Sheba.objects.get(serviceprice=request.GET['serviceprice'])
        print(serviceprice,servicetitle)

        # cart = Cart(user=user_id,service=service_id)
        # cart = Cartanother(user=user_id,service=service_id,servicetitle=servicetitle,serviceprice=serviceprice)
        cart = Cartanothernew(user=user_id,service=service_id,servicetitle=servicetitle,serviceprice=serviceprice,serviceuseridnum=serviceuseridnum)
        cart.save()
        # return redirect('serviceshow')
        return redirect('buyerdashboard')
        # return JsonResponse({'usr': user_id,'service':service_id})
        # fm = Service()
    # else:
    #     fm = Service()
    # return render(request,'service/5servicepage.html',{"form":fm})

#new admin panel
# def newadminpanel(request):
#     return render(request,'adminpanel/cartDashboard.html')

# def servicelist(request):
#     return render(request,'adminpanel/allservicelist.html')

# def alluserlist(request):
#     return render(request,'adminpanel/alluserlist.html')

def cartItemDelete(request,id):
    if request.method =='GET':
        # data_id =  Cartanother.objects.get(id=id) 
        data_id =  Cartanothernew.objects.get(id=id)
        data_id.delete()
        print(data_id)
    return redirect('buyerdashboard')

def order(request):
    if request.method =="POST":
        cartid = request.POST['cartid']
        serviceuserid=request.POST['serviceuserid']
        userid = request.POST['userid']
        serviceid = request.POST['serviceid']
        servicetitle = request.POST['servicetitle']
        serviceprice = request.POST['serviceprice']
        date = request.POST['date']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        # order = Order(cartid=cartid,userid=userid,serviceid=serviceid,orderservicetitle=servicetitle,orderserviceprice=serviceprice,orderdate=date,orderaddress=address,orderphoneno=phoneno)
        # order.save()
        ordernew = Ordernew(cartid=cartid,userid=userid,serviceuserid=serviceuserid,serviceid=serviceid,orderservicetitle=servicetitle,orderserviceprice=serviceprice,orderdate=date,orderaddress=address,orderphoneno=phoneno)
        ordernew.save()
        cartdelete =Cartanothernew.objects.get(id=cartid)
        cartdelete.delete()
        print(cartid,userid,serviceid,servicetitle,serviceprice,date,address,phoneno)

    return redirect('buyerdashboard')
