from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm,MyPasswordChangeForm


urlpatterns = [

    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('shop/',views.shop,name="shop"),
    path('shop/<str:slug>',views.Product,name="Product"),
    path('shop/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name="add_to_wishlist"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views. signuppage,name="signup"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logout,name="logout"),
    path('mywishlist/',views.mywishlist,name="mywishlist"),
    path('remove_from_wishlist/<int:id>/',views.remove_from_wishlist,name="remove_from_wishlist"),
    path('mycart/',views.mycart,name="mycart"),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name="add_to_cart"),
    path('remove_from_cart/<int:id>/',views.remove_from_cart,name="remove_from_cart"),
    path('change_qty/<int:pk>/',views.change_qty,name="change_qty"),
    path('checkout/',views.checkout,name="checkout"),
    path('mycheckout/',views.mycheckout,name="mycheckout"),
    path('myorder/',views.myorder,name="myorder"),
    path('placeorder/',views.placeorder,name="placeorder"),
    path('confirmorder/',views.confirmorder,name="confirmorder"),
    path('view-order/<str:t_no>',views.orderview,name="orderview"),


    #reset password url
    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_Confirm"),
    path('reset/Done/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_Complete"),

    #change password url
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',form_class= MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    
]