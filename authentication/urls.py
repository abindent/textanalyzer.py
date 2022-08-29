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

from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from .views import *


def login_forbidden(function=None, login_url: str = "/", redirect_field_name: str = "unknown"):
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)

    return actual_decorator

urlpatterns = [

    # FRONTEND AUTHENTICATION PAGE
    path("login", login, name="login"),
    path("signup", register, name="signup"),

    ## LOGOUT ROUTE
    path("logout", handelLogout, name="logout"),

    
    

    ## RESET PASSWORD VIEW
    path("forgot_password/reset/", login_forbidden(PasswordReset.as_view(), "/", "authenticated_user_redirect_from"),name="password_reset"),
    path("forgot_password/reset/done/", login_forbidden(PasswordResetDone.as_view(), "/", "authenticated_user_redirect_from"), name="password_reset_done"),
    path("forgot_password/reset/<uidb64>/<token>/", login_forbidden(PasswordResetConfirm.as_view(), "/", "authenticated_user_redirect_from"), name="password_reset_confirm"),
    path("forgot_password/reset/complete/", login_forbidden(PasswordResetComplete.as_view(), "/", "authenticated_user_redirect_from"), name="password_reset_complete"),

]
