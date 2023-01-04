from django.db import models
from account.models import User
from service.models import Sheba
# Create your models here.

class Cartanother(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Sheba,on_delete=models.CASCADE)
    servicetitle =  models.CharField(max_length=300)
    serviceprice =  models.CharField(max_length=300)