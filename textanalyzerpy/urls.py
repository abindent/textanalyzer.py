"""textanalyzerpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.views.static import serve

admin.site.site_header="Text Analyzer Admin"
admin.site.site_title="Text Analyzer Admin Panel"
admin.site.index_title="Welcome to Text Analyzer Admin Panel"


urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # STATIC AND MEDIA
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    # MAIN WEBSITE PAGES AND LOGICS
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('analyzer/', views.analyzer, name='analyzer'),

    path('analyzed', views.analyzed, name='analyzed'),

    path('editor/', views.designer, name='editor'),

    path('styler/', views.styler, name='styler'),

    path('contact/', views.contact, name='contact'),

    path('submit', views.submit, name='submit'),

    # BLOGS RELATED
    path('blog/', include('blog.urls')),

    path('search', views.search, name="search"),
    
    # LOGIN, LOGOUT, REGISTER
    path('signup', views.handleSignUp, name="handleSignUp"),

    path('login', views.handeLogin, name="handeLogin"),

    path('logout', views.handelLogout, name="handelLogout"),

    # PROFILE AND ACCOUNT DETAILS UPDATION
    path('profile/', views.UserEditingView.as_view(), name="profile"),

    path('profile/v2', views.profilev2, name="profilev2"),

    path('password/', views.UpdatingPasswordView.as_view(), name="password"),

    path('password_success/', views.password_success, name="password_sucess"),

    # DELETE ACCOUNT FUNCTION
    path("delete_account", views.delete_account, name="delete_account"),
   
    # ADDITIONAL PROFILE DETAILS CHANGER
    path('change_photo', views.change_photo, name="change_photo"),

    # FORGOT PASSWORD
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="auth/password-reset.html"), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="auth/password-reset-sent.html"), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_changed.html"), name='password_reset_complete'),

 ]

handler404 = 'textanalyzerpy.views.error_404_views'
handler500 = 'textanalyzerpy.views.error_500_views'

