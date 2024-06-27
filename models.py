from email.policy import default
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
import datetime
import os

# Create your models here.

def get_file_path(request,filename):
    original_filename = filename
    nowtime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowtime, original_filename)
    return os.path.join('uploads/',filename)

class User(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=250)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.fname+" - "+self.lname  

class Categorys(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)
    slug = models.CharField(max_length=150,null=False,blank=False ,default="")
    image = models.ImageField(upload_to=get_file_path, null=True,blank=False)
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    description = models.TextField(max_length=500,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=False,blank=False)
    slug = models.CharField(max_length=150,null=False,blank=False ,default="")
    product_image = models.ImageField(upload_to=get_file_path, null=True,blank=False)
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    quntitly=models.IntegerField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    original_price =models.FloatField(null=False,blank=False)
    selling_price =models.FloatField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.fname+" - "+self.product.slug


class Contact(models.Model):
    name=models.CharField(max_length=20,validators=[RegexValidator(r'^[a-zA-Z]+$', message='Name should only contain letters.')])
    email=models.CharField(max_length=25)
    Mobile=models.CharField(max_length=10)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    product_qty=models.PositiveIntegerField()
    product_price=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()
    payment_status=models.BooleanField(default=False)


    def __str__(self):
        return self.user.fname+" - "+self.product.slug


class orderdetails(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    Mobile=models.CharField(max_length=10)
    pincode=models.IntegerField(null=False,blank=False)
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    mobile=models.CharField(max_length=10)
    pincode=models.IntegerField(null=False,blank=False)
    address=models.CharField(max_length=250)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=False)
    orderstatues = (
        ('pending','Pending'),
        ('Out for shipping','Out For Shipping'),
        ('Completed','Completed'),

    )
    status=models.CharField(max_length=150,choices=orderstatues,default='Pending')
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)



class orderitem(models.Model):
    order = models.ForeignKey(order,on_delete=models.CASCADE)
    product= models.ForeignKey(Products,on_delete=models.CASCADE)
    price= models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id,self.order.tracking_no)



