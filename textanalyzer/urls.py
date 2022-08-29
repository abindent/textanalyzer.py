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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve


admin.site.site_header="Text Analyzer Admin"
admin.site.site_title="Text Analyzer Admin Panel"
admin.site.index_title="Welcome to Text Analyzer Admin Panel"

urlpatterns = [

    ## STATIC AND MEDIA ENDPOINTS
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),


    ## ADMIN ENDPOINTS
    path('admin/', admin.site.urls),

    ## AUTHENTICATION ENDPOINTS
    path('auth/', include('authentication.urls')),
    
    ## API ENDPOINTS
    path('api/', include('api.urls')),

    ## PROFILE AND ACCOUNT RELATED ENDPOINTS
    path("user/", include('member.urls')),  

    ## SEARCH ENDPOINTS
    path("search/", include("search.urls")),
  
    ## FRONTEND ENDPOINTS

    ### WEBSITE MAIN PAGES  FRONTEND ENDPOINTS
    path('', include('home.urls')),


    ### TOOLS FRONTEND ENDPOINT
    path('tools/', include('tools.urls')),

    ### BLOG FRONTEND ENDPOINTS
    path('blog/', include('blog.urls')), 

] 

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'