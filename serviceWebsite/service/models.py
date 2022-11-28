from django.db import models
from django.conf import settings
from account.models import User
# Create your models here.
class Sheba(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    servicecategory =(
        ('service1','service1'),
        ('service2','service2'),
        ('service3','service3'),
        ('service4','service4'),
    )
    servicelocation=(
        ('Dhaka','Dhaka'),
        ('Chittagong','Chattagram')
    )
    servicetitle = models.CharField(max_length=100)
    servicedetails = models.CharField(max_length=100)
    servicecategory = models.CharField(max_length=100,choices=servicecategory,default='service1')
    serviceprice = models.IntegerField(max_length=100)
    servicelocation = models.CharField(max_length=10,choices=servicelocation,default='Dhaka')