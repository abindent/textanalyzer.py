from typing import ContextManager
from django.contrib.messages.api import success
from django.forms.widgets import FileInput
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from blog.models import Post
from django.contrib.auth import authenticate,  login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from members.forms import *
from members.models import *
import os
from contact.models import *
from functools import partial
import random

# New Code


def index(request):
     return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def analyzer(request):
    return render(request, 'analyzer.html')


def styler(request):
    return render(request, 'styler.html')


def designer(request):
    return render(request, "designer.html")


def contact(request):
    return render(request, "contact.html")


def analyzed(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    removenum = request.POST.get('removenum', 'off')
    removealpha = request.POST.get('remalpha', 'off')
    lowercaps = request.POST.get('lowercaps', 'off')
    remspecialchar = request.POST.get('remspecialchar', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removenum == "on"):
        nos = '1234567890'
        analyzed = ""
        for char in djtext:
            if char not in nos:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removealpha == "on"):
        alphas = 'abcdefghijklmnopqurstuvwxyz'
        analyzed = ""
        for char in djtext:
            if char not in alphas:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Alphabets', 'analyzed_text': analyzed}
        djtext = analyzed

    if(remspecialchar == "on"):
        specialchar = ''' !"#$%&'()*+,-./:‸⁁⎀;‱©†¤©‡(ɔ)<=>?@[\]^_`{|}~⟨ ⟩⁂±¶®℗™∴'''
        analyzed = ""
        for char in djtext:
            if char not in specialchar:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Special Characters',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(lowercaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()

        params = {'purpose': 'Changed to lowercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1

        params = {'purpose': 'Counting no. of characters in your input',
                  'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and lowercaps != "on" and charcount != "on" and removenum != "on" and removealpha != "on" and remspecialchar != "on"):
        analyzed = "please select any operation and try again"
        params = {'purpose': 'Error Occured', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)


def error_404_views(request, exception):
    return render(request, '404.html')


def error_500_views(request):
    return render(request, '500.html')



def submit(request):

  if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        content = request.POST['content']
        if  Contact.DoesNotExist:
         if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
             messages.error(request, "Please fill the form correctly")
             return redirect("/contact")
         if request.user.is_authenticated:
             contact= Contact(user=request.user,name=name, email=email, phone=phone, content=content)
             contact.save()
             messages.success(request, "Your message has been successfully sent")
             return redirect("/contact")
        else:
             messages.error(request, "Already submitted your query.")
             return redirect("/contact")
     
  else:
        messages.error(request, "Please log in before posting your query.")
        return redirect("/contact")
 
def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query.")
    if query == "":
        messages.warning(request, "Please enter something to search")
        return redirect("/")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'search.html', params)


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('/')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, " Your Text Analyzer account has been successfully created")
        return redirect('/')

    else:
        return redirect("/error")


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
         
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return redirect("/error")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')


@login_required(login_url="/")
def change_photo(request):
 try: 
     profile = request.user.profile
 except  Profile.DoesNotExist:
    bio = request.POST['bio']
    profile_pic = request.FILES['profile_pic']
    profile2 = Profile(user=request.user, bio=bio, profile_pic=profile_pic)
    profile2.save()
 
 if request.method == 'POST':
     form = UserProfileForm(request.POST,request.FILES, instance=profile)
     if form.is_valid :
         form.save()
         messages.success(request, "Profile Upfated Successsfully")
         return redirect('profile/v2')
     else:
         messages.error(request, "Failed")
         return redirect('profile/v2')

 return redirect('profile/v2')  

@login_required(login_url="/")      
def profilev2(request):
    context = {"form": UserProfileForm}
    return render(request, 'profile/pic.html', context)


class UserEditingView(generic.UpdateView):
    form_class = UserEditingForm
    template_name = "profile/profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class UpdatingPasswordView(PasswordChangeView):
    form_class = PasswordUpdateForm
    template_name = "profile/password.html"
    success_url = reverse_lazy('password_success')


def password_success(request):
    messages.success(
        request, " Your Text Analyzer account password has been successfully changed")
    return redirect("/")

def delete_account(request):
    if request.method == "POST":
        if request.user.is_superuser:
         messages.error(request, "YOU CANNOT DO THIS")
         return redirect("/")

        if request.user.is_staff:
         messages.error(request, "YOU CANNOT DO THIS")
         return redirect("/")

        else: 
          username = request.user.username
          del_user = User.objects.filter(username=username) 
          logout(request)
          del_user.delete()  
          messages.success(request, "Account Successfully Deleted")
          return redirect("/")

        
    return redirect("/profile")
