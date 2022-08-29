"""textanalyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard", index, name="dashboard"),
    path("info", UserDetailsUpdate.as_view(), name="update_user_info"),
    path("application", application_details, name="application_details"),

    ## EDITING PROFILE AND OTHER ACCOUNT DETAILS
    path("profile", ProfileEdit, name="update_profile"),
    path("password", PasswordChange.as_view(), name="update_password"),

    ## CREATING A PROFILE
    path("profile/create", create_profile, name="create_profile"),

    ## REDIRECTS
    path("info/redirect", info_redirect, name="info_redirect"),
    path("info/password/redirect", password_redirect, name="password_redirect"),

    ## CREATE AND VIEW BLOG FRONTEND
    path("blogs", view_blog, name="view_blog"),
    path("blogs/create", create_blog, name="create_blog"),

]