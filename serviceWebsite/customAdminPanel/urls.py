from django.urls import path,include
from customAdminPanel import views
urlpatterns = [
    ###working on dashboard
    path('newadminpanel', views.newadminpanel,name='dashboard'),
    path('servicelist', views.servicelist,name='servicelist'),
    path('alluserlist', views.alluserlist,name='userlist'),
]