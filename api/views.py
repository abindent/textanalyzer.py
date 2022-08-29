import re
from uuid import uuid4

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from api.models import *
from verify.models import VerifyUser
from member.models import Profile

from textanalyzer.constants import HOST
from textanalyzer.captcha import check_recpatcha, captchaVerificationFailedHandler
# Create your views here.

# CONTACT SUBMISSION
def submit_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['message']

        res = check_recpatcha(request)

        if res != True:
            captchaVerificationFailedHandler(request, res)
            return redirect("/contact")
        
        
        if request.user.is_authenticated:
            contact = Contact(name=name, email=email,
                            phone=phone, content=content)
            contact.save()
            messages.success(request, "Successfully submitted the form.")
            return redirect("/contact")
        else:
            messages.error(request, "Failed to submit form.")
            return redirect("/contact")

    return redirect("/contact")

# USER LOGIN
def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        identifier = request.POST['identifier']
        password = request.POST['password']

        res = check_recpatcha(request)

        if res != True:            
            captchaVerificationFailedHandler(request, res)
            return redirect("/auth/login")

    

        # User object and Verification
        if isValidEmail(identifier):
            _user_ = User.objects.filter(email=identifier).first()

        else:
            _user_ = User.objects.filter(username=identifier).first()

        if not _user_.is_superuser or not _user_.is_staff:

            _verification_profile_user = VerifyUser.objects.filter(
                user=_user_).first()

            if not _verification_profile_user.is_verified:
                messages.error(request, "This account is not verified.")
                return redirect('/auth/login')

            if _verification_profile_user.is_blocked:
                messages.warning(
                    request, "For violating any rule you have been blocked using your account. You might request an unblock to the admins.")
                return redirect('/auth/login')


        # Authentication
        if isValidEmail(identifier):
            new_user = User.objects.filter(email=identifier).first()
            user = authenticate(username=new_user.username, password=password)

        else:
            user = authenticate(username=identifier, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/user/dashboard")

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/auth/login")

    messages.warning(request, "You are already authenticated.")
    return redirect("/user/dashboard")

# USER SIGNUP
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        res = check_recpatcha(request)

        if res != True:            
            captchaVerificationFailedHandler(request, res)
            return redirect("/auth/signup")
 
        # check for errorneous input
        if len(username) < 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('/auth/signup')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('/auth/signup')

        if not isValidEmail(email):
            messages.error(request, "The email is invalid.")
            return redirect('/auth/signup')

        if (password != cpassword):
            messages.error(request, " Passwords do not match")
            return redirect('/auth/signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return redirect('/auth/signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User with this username already exists.")
            return redirect('/auth/signup')

        # CREATING THE USER
        myUser = User(username=username, email=email,
                    first_name=first_name, last_name=last_name)
        myUser.set_password(password)
        myUser.save()

        # CREATING VERIFIFCATION OBJECT
        token = str(uuid4())
        create_verification_profile(user=myUser, token=token)

        # SENDING EMAIL TO THE USER
        sendMail(username=username, email=email, subject="Your account needs to be verified.", template_path='email/account_activate.html', params={
                'username': username, 'token': token, 'host_uri': HOST.host_uri, "image_api_base_url": "https://res.cloudinary.com/opensourcegames/image/upload/v1655310955/TextAnalyser"})

        # SENDING SUCCESSS MESSAGE
        messages.success(
            request, "Successfully created your account. We have sent you an email with the account activation link. Check out that to activate your account then log in.")
        return redirect('/')

    messages.error(request, "Failed to create the account")
    return redirect("/auth/signup")


# PROFILE UPDATION
@login_required(login_url='/auth/login')
def update_profile(request):
    try:
        profile = Profile.objects.filter(user=request.user).first()

    except Profile.DoesNotExist:
        messages.error(request, "Please create a profile first.")
        return redirect('/user/profile/create')

    if request.method == 'POST':
       res = check_recpatcha(request)

       if res != True:            
            captchaVerificationFailedHandler(request, res)
            return redirect("/auth/signup") 
           
    try: 
        beta = bool(request.POST.get("beta"))
        bio = request.POST.get("bio", profile.bio) 

        avatar = request.FILES.get("avatar", None)

        profile.beta = beta
        profile.bio = bio

        if avatar:
            profile.avatar = avatar

        profile.save()     
        
        messages.success(request, "Profile Updated Successsfully")
        return redirect('/user/profile')

    except:
            messages.error(request, "Failed to save details.")
            return redirect('/user/profile')

    return redirect('/user/profile')

# PROFILE DELETION
@login_required(login_url='/auth/login')
def delete_profile(request):
    if request.method == "POST":
       res = check_recpatcha(request)

       if res != True:            
            captchaVerificationFailedHandler(request, res)
            return redirect("/auth/signup") 
           
       profile = Profile.objects.filter(user=request.user).first()
       profile.delete()

       messages.success(request, "Successfully deleted your profile.")
       return redirect("/user/dashboard")

    return redirect('/user/profile')

# ACCOUNT DELETION
@login_required(login_url='/auth/login')
def delete_account(request):
    if request.method == "POST":
        res = check_recpatcha(request)

        if res != True:            
            captchaVerificationFailedHandler(request, res)
            return redirect("/user/dashboard") 

        if request.user.is_superuser:
            messages.error(request, "A Superuser account cannot be deleted.")
            return redirect("/user/dashboard")

        if request.user.is_staff:
            messages.error(
                request, "A Staff account cannot be deleted without informing the admins.")
            return redirect("/user/dashboard")

        else:
            username = request.user.username
            del_user = User.objects.filter(username=username)
            logout(request)
            del_user.delete()
            messages.success(request, "Account Successfully Deleted.")
            return redirect("/")

    return redirect('/user/dashboard')


# VERIFICATION LOGICS

# CREATING VERIFICATION PROFILE
def create_verification_profile(user, token: str):

    try:
        verify_user_obj = VerifyUser(user=user, token=token)
        verify_user_obj.save()

    except:
        raise Exception('Failed to find a user or a method problem.')

# SENDMAIL FUNCTION
def sendMail(username: str, subject: str, email: str, template_path: str, params: dict):
    from_email = f"From <accounts@textanalyzerpy.herokuapp.com>"
    subject = subject

    html_body = render_to_string(template_path, params)
    plain_text = strip_tags(html_body)

    recipient_list = [email]
    send_mail(subject=subject, message=plain_text, html_message=html_body,
              from_email=from_email, recipient_list=recipient_list, fail_silently=False)

# ACCOUNT VERIFICATION
def verify(request, token: str):
    verifiction_user_profile = VerifyUser.objects.filter(
        token=token).first()

    if verifiction_user_profile:
        verifiction_user_profile.is_verified = True
        verifiction_user_profile.save()
        sendMail(username=verifiction_user_profile.user.username, subject="Welcome to TextAnalyzer", email=verifiction_user_profile.user.email, template_path='email/account_activate_complete.html', params={"username": verifiction_user_profile.user.username})
        messages.success(request, 'Successfully verified your email.')
        return redirect('/auth/login')

    else:
        messages.error(request, "Verification Failed")
        return redirect('/auth/login')


# UTILS
def isValidEmail(string: str) -> bool:
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    return True if re.fullmatch(regex, string) else False

