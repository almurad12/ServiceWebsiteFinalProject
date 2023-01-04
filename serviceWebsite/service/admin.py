from django.contrib import admin
from .models import User
from .models import Sheba
from cart.models import Cart,CartOne
# Register your models here.
admin.site.register(User)
admin.site.register(Sheba)
admin.site.register(Cart)
admin.site.register(CartOne)