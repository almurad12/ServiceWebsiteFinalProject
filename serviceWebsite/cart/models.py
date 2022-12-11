from django.db import models

# from .models import User
# from .models import Sheba

from account.models import User
from service.models import Sheba


# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Sheba,on_delete=models.CASCADE)
    
