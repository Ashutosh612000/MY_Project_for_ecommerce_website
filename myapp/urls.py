
from django.urls import path
from .views import *

urlpatterns = [
    path('signupbuyer/',handle_Signup_for_Buyer,name='signupbuyer'),
    path('signupseller/',handle_Signup_for_Seller,name='signupseller'),
    path('login/',handlelogin,name='handlelogin'),
    path('logout/',handlelogout,name='handlelogout'),
    path('',home,name='home'),
]
