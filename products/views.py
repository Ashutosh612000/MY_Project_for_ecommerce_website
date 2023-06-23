from django.shortcuts import render
from .models import *

# Create your views here.
def product_seller(request):
    if request.method == 'POST':
        name = request.POST['product_name']
        price = request.POST['price']
        description = request.POST['description']
        category = request.POST['category']
        image = request.POST['image']
        user = request.POST['user']

        p = Product(name=name, price=price, description=description, category=category, image=image)
        p.save()

    return render(request,'tempaltes/seller/seller.html')


def Show_product(request,pname):
    show_user = Category.objects.all()
    print(show_user)
    print('================================================================')

    return render(request,'base.html' , {'show_user': show_user})



