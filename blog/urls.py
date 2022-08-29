"""textanalyzerpy Blog Page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4/topics/http/urls/
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
    ## POST, EDIT OR DELETE COMMENTS API
    path('post/comment', postComment, name="post_comment"),
    path('delete/comment/<str:slug>/<int:sno>', deleteComment, name="delete_comment"),
    path('edit/comment/<str:slug>/<int:sno>', editComment, name="edit_comment"),

    ## ADD A BLOG
    path('create/<int:sno>', create_blog, name="add_a_blog"),
    
    ## BLOG HOME PAGE FRONTEND 
    path('', index, name="blog_home_page"),

    ## PARTICULAR BLOG PAGE FRONTEND
    path('<str:slug>', blog, name="blog_post_page"),
]

