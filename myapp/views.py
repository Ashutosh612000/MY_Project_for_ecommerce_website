from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from myapp.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login,logout
from products.models import Category
from products.views import product_seller


# def home(request):
#     return render('home.html')

def home(request):
    show_user = Category.objects.all()
    return render(request, 'home.html',{'show_user': show_user})

def handle_Signup_for_Buyer(request):
    show_user = Category.objects.all()
    if request.method == 'POST':
            #Get teh post parameters
            
            fname=request.POST['fname']
            lname=request.POST['lname']
            mobile=request.POST['mobile']
            email=request.POST['email']
            user_type='buyer'
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']

            subject="test email"
            context = {
                'name': fname, 
                'email': email, 
                'num': mobile,
                'user_type' : user_type,
            }
            
            # message = render_to_string('msg.html', context)
            # new_message = strip_tags(message)
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email]

            # send_mail(subject,new_message , email_from , recipient_list,fail_silently=False,)
            
        

        


            if pass1 != pass2:
                messages.error(request, 'password dose not match')
                return redirect('home')
            
            myuser = User.objects.create_user(email,pass1)
            
            myuser.first_name =fname
            myuser.last_name =lname
            myuser.mobile = mobile
            myuser.user_type = user_type
            myuser.save()
        
            messages.success(request, "Profile details updated.")
            
            return redirect('home') 
    return render(request, 'signupbuyer.html',{'show_user': show_user})




def handle_Signup_for_Seller(request):
    show_user = Category.objects.all()
    if request.method == 'POST':
            #Get teh post parameters
            
            fname=request.POST['fname']
            lname=request.POST['lname']
            mobile=request.POST['mobile']
            email=request.POST['email']
            user_type='seller'
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']

            subject="test email"
            context = {
                'name': fname, 
                'email': email, 
                'num': mobile,
                'user_type' : user_type,
            }
            
            # message = render_to_string('msg.html', context)
            # new_message = strip_tags(message)
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email]

            # send_mail(subject,new_message , email_from , recipient_list,fail_silently=False,)
            
        

        


            if pass1 != pass2:
                messages.error(request, 'password dose not match')
                return redirect('handleSignup')
            
            myuser = User.objects.create_user(email,pass1)
            
            myuser.first_name =fname
            myuser.last_name =lname
            myuser.mobile = mobile
            myuser.user_type = user_type
            myuser.save()
        
            messages.success(request, "Profile details updated.")
            
            return redirect('sellerhome') 
    return render(request, 'signupseller.html',{'show_user': show_user})


def handlelogin(request):
    show_user = Category.objects.all()
    if request.method == 'POST':
        loginemail = request.POST.get('loginemail') 
        loginpass = request.POST.get('loginpass')  

        user = authenticate(email=loginemail, password=loginpass) 

        if user is not None:
            login(request, user)  # Log in the authenticated user

            if user.user_type == 'seller': 
                return redirect('sellerhome') 
            else:
                return redirect('home') 

            messages.success(request, "Login successful") 
            return redirect('home')  
        else:
            messages.error(request, "Invalid details")
            return redirect('home')  
    return render(request, 'login.html',{'show_user': show_user})

def handlelogout(request):
        logout(request)
        messages.success(request, "Successfully logged out") 
        return redirect('home')

# def handlelogout(request):
#     logout(request)
#     messages.success(request, 'Logout successfully')
#     return redirect('index')

# def Seller(request):
#     return render(request, 'seller/sellerhome.html')