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
from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header="Text Analyzer Admin"
admin.site.site_title="Text Analyzer Admin Panel"
admin.site.index_title="Welcome to Text Analyzer Admin Panel"


urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('analyzer/', views.analyzer, name='analyzer'),

    path('analyzed', views.analyzed, name='analyzed'),

    path('editor/', views.designer, name='editor'),

    path('styler/', views.styler, name='styler'),

    path('contact/', views.contact, name='contact'),

    path('submit', views.submit, name='submit'),

    path('blog/', include('blog.urls')),

    path('search', views.search, name="search"),

    path('signup', views.handleSignUp, name="handleSignUp"),

    path('login', views.handeLogin, name="handeLogin"),

    path('logout', views.handelLogout, name="handelLogout"),


 ]

handler404 = 'textanalyzerpy.views.error_404_views'
handler500 = 'textanalyzerpy.views.error_500_views'

