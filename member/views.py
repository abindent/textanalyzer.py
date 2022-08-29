from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from application.models import Application
from member.forms import USEREDITFORM, PASSWORDUPDATINGFORM
from member.models import Profile
from blog.models import Blog

from textanalyzer.captcha import check_recpatcha, captchaVerificationFailedHandler
# Create your views here.

## MAIN DASHBAORD PAGE
@login_required(login_url="/auth/login")
def index(request):
    return render(request, "auth/dashboard/dash.html")

## APPLICATION DETAILS
@login_required(login_url="/auth/login")
def application_details(request):

    applications = Application.objects.filter(user=request.user).all()
    context = {"applications": applications}
    return render(request, "auth/dashboard/dash_application.html", context=context)

## PROFILE CREATION
def create_profile(request):
       
    if request.method == 'POST':
        beta = request.POST.get('beta', False)

        res = check_recpatcha(request)

        if res != True:
            captchaVerificationFailedHandler(request, res)
            return redirect("/user/profile/create")

        if beta == "on":
            beta  = True

        bio = request.POST.get("bio", None)

        avatar = request.FILES.get("avatar", None) 

        if avatar is not None:
            profile = Profile.objects.create(user=request.user, bio=bio, beta=beta, avatar=avatar)

        else:
            profile = Profile.objects.create(user=request.user, bio=bio, beta=beta)

        profile.save()    

        messages.success(request, 'Successfully created your profile.')
        return redirect('/user/profile')    

    else:
        try: 
            profile = request.user.profile
            return redirect('/user/profile')  
        except Profile.DoesNotExist:
          return render(request, 'auth/operations/create_profile.html')
        

## EDITING PROFILE
@login_required(login_url="/auth/login")
def ProfileEdit(request):
    try: 
        profile = request.user.profile
    except Profile.DoesNotExist:
        messages.error(request, 'Please create a profile first.')
        return redirect('/user/profile/create')

    return render(request, 'auth/dashboard/profile.html')

##  CUSTOM REDIRECTS   
def info_redirect(request):
    messages.success(request, "Your account details has been successfully changed.")
    return redirect('/user/info')

def password_redirect(request):
    messages.success(request, "Account password has been successfully changed.")
    return redirect('/user/info')

## CLASS BASED FUNCTIONS

### INFO PAGE TO UPDATE USER DETAILS
class UserDetailsUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = "/auth/login"
    redirect_field_name = "#"
    form_class = USEREDITFORM
    template_name = 'auth/dashboard/user_info.html'
    success_url = reverse_lazy('info_redirect')

    def get_object(self):
        return self.request.user

### A PAGE TO UPDATE ACCOUNT PASSWORD
class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    login_url = "/auth/login"
    redirect_field_name = "#"
    form_class = PASSWORDUPDATINGFORM
    template_name = 'auth/operations/change_password.html'
    success_url = reverse_lazy('password_redirect')


## CREATE AND VIEW BLOG FRONTEND
@login_required(login_url="/auth/login")
def create_blog(request):
    return render(request, 'auth/dashboard/create_blog.html')   

@login_required(login_url="/auth/login")
def view_blog(request):
    blogs = Blog.objects.filter(user=request.user).all()
    return render(request, 'auth/dashboard/view_blog.html', {"blogs": blogs})   