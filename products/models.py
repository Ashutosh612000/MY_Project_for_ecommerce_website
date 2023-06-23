from django.db import models
from myapp.models import User


class Category(models.Model):
    category_type =[
        ('mobile','mobile'),
        ('charger','charger'),
        ('earphone','earphone'),
    ]
    
    category_name= models.CharField(max_length=10,choices=category_type,default='mobile')

    def __str__(self):
        return self.category_name
    

class Comapny(models.Model):
    company_name = [
        ('samsung','samsung'),
        ('vivo','vivo'),
        ('apple','apple'),
        ('google','google'),
        ('boat','boat')
    ]

    company_name = models.CharField(max_length=20, choices=company_name, default='apple')

    def __str__(self):
        return self.company_name

class Product(models.Model):
    product_name= models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=8,decimal_places=2)
    product_description = models.TextField(max_length=500)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_comapny = models.ForeignKey(Comapny, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='static/images/')
    product_qunitity = models.PositiveIntegerField()
    product_user = models.ForeignKey(User, on_delete=models.CASCADE)







