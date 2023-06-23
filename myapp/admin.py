from django.contrib import admin
from myapp.models import User
# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display =['email', 'user_type']


admin.site.register(User,useradmin)