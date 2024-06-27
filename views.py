import email
from functools import total_ordering
from itertools import product
from unicodedata import category
from django.shortcuts import render,redirect
from .models import Categorys,Products, User,WishList,Contact,Cart,orderdetails,order,orderitem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
import random
# Create your views here.

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def shop(request):
    Category=Categorys.objects.all()
    context = {'category':Category}
    return render(request,'shop.html',context)  

def Product(request,slug):
    if(Categorys.objects.filter(slug=slug,status=0)):
        products=Products.objects.filter(category__slug=slug)
        category = Categorys.objects.filter(slug=slug).first()
        context = {'products':products,'category':category}
        return render(request,"product.html",context)
    else:
        messages.warning(request,"No such category found ")
        return redirect('shop')

def productview(request,cate_slug ,prod_slug):
    if(Categorys.objects.filter(slug=cate_slug,status=0)):
            if(Products.objects.filter(slug=prod_slug,status=0)):
                products=Products.objects.filter(slug=prod_slug,status=0).first
                context = {'products':products}
            else:  
                messages.error(request,"No such product found ")
                return redirect('shop')
    else:
        messages.error(request,"No such category found ")
        return redirect('shop')

    return render(request,"productview.html",context)


def add_to_wishlist(request,pk):
    product=Products.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    WishList.objects.create(user=user,product=product)
    return redirect('mywishlist')


def remove_from_wishlist(request,id):
    user=User.objects.get(email=request.session['email'])
    product=Products.objects.get(id=id)
    wishlist=WishList.objects.filter(user=user,product=product)
    wishlist.delete()
    messages.success(request,'Product Remove From Wishlist')
    return redirect('mywishlist')

    

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            Mobile=request.POST['Mobile'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')


def signuppage(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email already Registered"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['password']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    
                )  
                msg="User Sign Up Sucessfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="Password & Confirm Password Does not Matched"
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')

def loginpage(request):
    if request.method=="POST":
        try:
            user=User.objects.get(
                email=request.POST['email'],
                password=request.POST['password'],
            )
            request.session['email']=user.email
            request.session['fname']=user.fname
            return render(request,'home.html')
        except:
            msg="Email or Password Is Incorrect"
            return render(request,'login.html',{'msg':msg})

    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')


def mywishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlist=WishList.objects.filter(user=user)
    return render(request,'mywishlist.html',{'wishlist':wishlist})


def add_to_cart(request,pk):
    product=Products.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(
        user=user,
        product=product,
        product_qty=1,
        product_price=product.selling_price,
        total_price=product.selling_price, 
    )
    return redirect('mycart')

def mycart(request):
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user)
    amount=0
    for p in carts:
        value = p.product_qty*p.product_price
        amount = amount + value
    totalamount = amount + 50
    return render(request,'mycart.html',{'carts':carts,'totalamount':totalamount,'amount':amount})


def remove_from_cart(request,id):
    user=User.objects.get(email=request.session['email'])
    product=Products.objects.get(id=id)
    cart=Cart.objects.filter(user=user,product=product)
    cart.delete()
    messages.success(request,'Product Remove From cart')
    return redirect('mycart')


def change_qty(request,pk):
    cart=Cart.objects.get(pk=pk)
    cart.product_qty=int(request.POST['product_qty'])
    cart.total_price=cart.product_qty*cart.product_price
    cart.save()
    return redirect('mycart')


def checkout(request):
    if request.method=="POST":
        orderdetails.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            Mobile=request.POST['Mobile'],
            pincode=request.POST['pincode'],
            address=request.POST['address'],
        )
        return redirect('mycheckout')
    else:
        return redirect('mycheckout')

def mycheckout(request):
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user)
    amount=0
    for p in carts:
        value = p.product_qty*p.product_price
        amount = amount + value
    totalamount = amount + 50
    return render(request,'checkout.html',{'carts':carts,'totalamount':totalamount,'amount':amount})


def myorder(request):
    user=User.objects.get(email=request.session['email'])
    orders = order.objects.filter(user=user)
    context ={'orders':orders}
    return render(request,'myorder.html',context)


def confirmorder(request):
    return render(request,'confirmorder.html')


def placeorder(request):
    if request.method == "POST":
        neworder = order()
        user=User.objects.get(email=request.session['email'])
        neworder.user=user
        neworder.name=request.POST.get('name')
        neworder.email=request.POST.get('email')
        neworder.mobile=request.POST.get('mobile')
        neworder.pincode=request.POST.get('pincode')
        neworder.address=request.POST.get('address')
        neworder.payment_mode=request.POST.get('payment_mode')

        user=User.objects.get(email=request.session['email'])
        carts=Cart.objects.filter(user=user)
        cart_total_price = 0
        for item in carts:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno = 'admin'+str(random.randint(1111111,9999999))
        while order.objects.filter(tracking_no=trackno) is None:
            trackno = 'admin'+str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno
        neworder.save()
        
        user=User.objects.get(email=request.session['email'])
        neworderitems=Cart.objects.filter(user=user)
        for item in neworderitems:
            orderitem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )
           
            orderproduct =Products.objects.filter(id=item.product_id).first()
            orderproduct.quntitly = orderproduct.quntitly - item.product_qty
            orderproduct.save()

        Cart.objects.filter(user=user).delete()

        messages.success(request,"Your order has been placed successfully")
    return redirect('confirmorder')



def orderview(request, t_no):
    user=User.objects.get(email=request.session['email'])
    Order=order.objects.filter(tracking_no=t_no).filter(user=user).first()
    orderitems=orderitem.objects.filter(order=Order)
    context={'order':Order,'orderitems':orderitems}
    return render(request,"orderview.html",context)
