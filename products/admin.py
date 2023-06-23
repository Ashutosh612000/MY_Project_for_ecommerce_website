from django.contrib import admin
from products.models import Category,Comapny,Product
# Register your models here.


class Category_Admin(admin.ModelAdmin):
    list_display = ['category_name']


class Company_Admin(admin.ModelAdmin):
    list_display =['company_name']

class Product_Admin(admin.ModelAdmin):
    list_display = ['product_name','product_category','product_comapny','product_user']



admin.site.register(Category,Category_Admin)
admin.site.register(Comapny,Company_Admin)
admin.site.register(Product,Product_Admin)
