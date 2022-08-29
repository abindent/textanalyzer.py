from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


#Create your views here.

def login(request):
   if request.user.is_authenticated: 
       messages.warning(request, "You have already logged in.")
       return redirect('/')
   
   return render(request, "auth/login.html")

def register(request):
   if request.user.is_authenticated:  
       messages.warning(request, "You have already logged in.")
       return redirect('/')
       
   return render(request, "auth/register.html")

def handelLogout(request):
   if request.method == "POST": 
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('/')

    return redirect("/")    
    
   return redirect("/")    
    

## RESET PASSWORD
class PasswordReset(PasswordResetView):
    template_name = "auth/operations/password_reset/index.html"
    html_email_template_name = "email/password_reset.html"
    
class PasswordResetDone(PasswordResetDoneView):
    template_name = "auth/operations/password_reset/done.html"

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "auth/operations/password_reset/confirm.html"
    

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "auth/operations/password_reset/complete.html"


