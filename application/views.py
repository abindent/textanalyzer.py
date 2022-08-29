from django.contrib import messages
from django.shortcuts import render, redirect

from application.models import Application

from textanalyzer.captcha import check_recpatcha, captchaVerificationFailedHandler

# Create your views here.
def index(request):

   if request.user.is_authenticated:
    return render(request, "application/index.html")

   messages.info(request, "Login to apply.")
   return redirect("/auth/login")

def register(request):
  if request.method == "POST":
    name = request.POST.get('name', None)
    reason = request.POST.get('reason', None)
    options = request.POST.get('options', None)
    
    res = check_recpatcha(request)

    if res != True:
      captchaVerificationFailedHandler(request, res)
      return redirect("/application")
    
    try:
      application = Application.objects.filter(user=request.user,options=options).first()

      if not application:

        Application.objects.create(user=request.user, name=name, reason=reason, options=options)
    
        messages.success(request, "Application successfully created.")
        return redirect("/application")

      else:
        messages.error(request, f"You have already applied for {option_to_text(application.options)}.")
        return redirect("/application")

    except:
      messages.error(request, "Failed to register your application.")
      return redirect("/application")

## DELETE OR EDIT AN APPLICATION
def edit_application(request, id):
  if request.method == "POST":
    application = Application.objects.get(id=id)
    reason = request.POST.get("reason", application.reason)
    application.reason = reason

    res = check_recpatcha(request)

    if res != True:
      captchaVerificationFailedHandler(request, res)
      return redirect("/application")
          
    if application.user == request.user:
      application.save()

      messages.success(request, "Successfully edited your application")
      return redirect("/user/application")
      
    messages.error(request, "This application does not belong to you, so don't try to edit.")
    return redirect("/user/application")  

  return redirect("/user/application")  

def delete_application(request, id):
  if request.method == "POST":
    application = Application.objects.get(id=id)

    if application.user == request.user:
      application.delete()

      messages.success(request, "Successfully deleted your application")
      return redirect("/user/application")

    messages.error(request, "This application does not belong to you, so don't try to delete.")
    return redirect("/user/application")  

  return redirect("/user/application")  

## UTILITY FUNCTIONS
def option_to_text(option: str) -> str:
  list ={
    "AD": "admin post",
    "ST": "staff post",
    "BW": "access to wrtie a blog."
  }
  return list[option]