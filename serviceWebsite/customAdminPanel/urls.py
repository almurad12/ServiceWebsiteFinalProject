from django.urls import path,include
from customAdminPanel import views
urlpatterns = [
    ###working on dashboard
    path('newadminpanel', views.newadminpanel,name='dashboard'),
    path('userlist', views.userlist,name='userlist'),
    path('userlist/<id>/delete', views.userlistdelete,name='userlistdelete'),
    ##allservicelist
    path('allservicelist',views.servicelist,name="allservicelist"),
    path('allservicelist/delete',views.servicelistdelete),
    ##all pending order
    path('allpendingorderlist', views.allpendingorderlist,name='allpendingorderlist'),
    path('allpendingorderlist/delete', views.pendingorderdelete,name='pendingorderdelete'),
    ##all order list
    path('allorderlist', views.allorderlist,name='allorderlist'),
    path('allorderlist/delete',views.allorderdelete,name="allorderdelete")
    # path('orderlist', views.orderlist,name='orderlist'),
]
