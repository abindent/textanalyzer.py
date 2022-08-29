from django.urls import path, include
from .views import *

urlpatterns = [

    ## CONTACT SUBMISSION ENDPOINT
    path("contact/submit", submit_contact, name="contact"),

    ## AUTHENTICATION ENDPOINT
    path("auth/login", handleLogin, name="login"),
    path("auth/signup", register ,name="singup"), 

    ## SOCIAL AUTH
    path(r'auth/social/', include('allauth.urls'), name="social_auth"),

    ## ACCOUNT VERIFICATION
    path("account/verify/<token>", verify, name="account_veirfy"),

    # ACCOUNT DELETION ENDPOINT
    path("account/delete", delete_account, name="delete_account"),

    ## PROFILE UPDATION ENDPOINT
    path("account/profile/update", update_profile, name="update_profile"),
    path("account/profile/delete", delete_profile, name="delete_profile"),

]

