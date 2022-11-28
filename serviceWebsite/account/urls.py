from django.urls import path
from account import views
urlpatterns = [
   path('', views.home, name='home'),
   # path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('sellerdashboard/',views.sellerdashboard, name='sellerdashboard'),
    path('buyerdashboard/',views.buyerdashboard, name='buyerdashboard'),
   #  path('adminpage/', views.admin, name='adminpage'),
   #  path('customer/', views.customer, name='customer'),
   #  path('employee/', views.employee, name='employee'),
]