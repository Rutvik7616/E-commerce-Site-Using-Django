from django.contrib import admin
from .models import User,Products,Categorys,WishList,Contact,Cart,orderdetails,order,orderitem

# Register your models here.
admin.site.register(User)
admin.site.register(Products)
admin.site.register(Categorys)
admin.site.register(WishList)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(orderdetails)
admin.site.register(order)
admin.site.register(orderitem)