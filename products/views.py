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

    return render(request,'seller/sellerhome.html')


def Show_product(request):
    show_category = Category.objects.all()
    print(show_category)
    print('================================================================')

    return render(request,'products.html' , {'show_category': show_category})

# def Show_product(request,pro):
#     category  = Category.objects.get(category_name=pro)
#     products  = Product.objects.filter(product_category=category)
    
    
#     return render(request,'products.html',{'products': products})









def Show_mobile(request,pro):
    # show = Product.objects.all()
    # category  = Category.objects.get(category_name=pro)
    # products  = Product.objects.filter(product_category=category)

    # for u in show:
    #     print('================================================================')
    #     print(u.product_name)
    return render(request,'mobile.html')