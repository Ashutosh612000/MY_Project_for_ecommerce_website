
from django.urls import path
from .views import *

urlpatterns = [
   
   path('Show_product/<str:pname>/',Show_product,name="Show_product"),
]
