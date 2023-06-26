
from django.urls import path
from .views import *

urlpatterns = [
   
   path('show_product/',Show_product,name="show_product"),
   path('show_mobile/<str:pro>/',Show_mobile,name="show_mobile"),
   # path('Show_product/<str:pro>/',Show_product,name="show_product"),
   
   path('sellerhome',product_seller,name='sellerhome'),
   # path('show_product/<str:pro>/',Show_product,name='show_product'),
]
