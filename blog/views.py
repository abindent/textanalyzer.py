from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count, Case, When
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from application.models import Application

from blog.models import Blog, Comment
from blog.templatetags import extras

from textanalyzer.captcha import check_recpatcha, captchaVerificationFailedHandler

# Create your views here.

## BLOG PAGE FRONTEND
def index(request):
    blogs = Blog.objects.all()
    not_published_blogs_count = len(Blog.objects.filter(publish=False).all())
    print(not_published_blogs_count)
   
    ___params={'blogs': blogs, 'blogisActive': "active", "not_published_blogs_count": not_published_blogs_count}

    return render(request, 'blog/index.html', ___params)

def blog(request, slug):

    blog=Blog.objects.filter(slug=slug).first()

    if blog:
        

        comments = Comment.objects.filter(post=blog, parent=None)
        replies = Comment.objects.filter(post=blog).exclude(parent=None)

        replyDict={}

        for reply in replies:
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno]=[reply]
            else:
                replyDict[reply.parent.sno].append(reply)

        context={'blogisActive': "active", 'post': blog, 'user': request.user, 'comments': comments, 'replyDict': replyDict}
    
        if blog.publish:    
            
          blog.views= blog.views + 1

          blog.save()
          
          return render(request, "blog/blog.html", context)

        else:
          if request.user.is_superuser and request.user.is_staff:
                return render(request, "blog/blog.html", context)
          
          messages.info(request, "This blog is not yet published. Please wait till it got approved by our admins.")
          return redirect("/blog/")  

    else:
        return redirect("/not-found?type='blog not found")        


## CREATE BLOG
def create_blog(request, sno):
    if request.method == "POST":

        _blog_title = request.POST.get('title', None)
        _blog_author_name = str(request.user.first_name + request.user.last_name)       
        _blog_gist = request.POST.get('gist', None)                                                                         
        _blog_content = request.POST.get('content', None)                                                   
        _blog_thumbnail = request.FILES.get('thumbnail', None) 

        res = check_recpatcha(request)  

        if res != True:
            captchaVerificationFailedHandler(request, res)
            return redirect("/user/blogs/create")
        
       
        _blog_slug = _blog_title.lower().replace(" ", "-").replace("/", "") 

        ___user = User.objects.get(id=sno)

        if not Application.objects.filter(options="AD", user= ___user).exists():
            messages.error(request, "You do not have permission to create a blog post.")
            return redirect("/user/blogs/create") 

        while Blog.objects.filter(slug=_blog_slug).exists():
            _blog_slug = _blog_slug + "-" + get_random_string(length=4)

    

        if(_blog_title is None or _blog_gist is None or _blog_content is None ):
            messages.error(request, "Please fill in all required fields.")
            return redirect("/user/blogs/create")  

        blog = Blog(title=_blog_title, user=request.user, author=_blog_author_name or "Unkwon Author", slug=_blog_slug, publish=False, gist=_blog_gist, content=_blog_content)

        if _blog_thumbnail is not None:
            blog.thumbnail = _blog_thumbnail

        blog.save()   

        messages.info(request, "Successfully added your blog. It is under observation. Please wait until we verify it and publish it.")
        return redirect("/user/blogs")  

    messages.error(request, "Sorry but you have not submitted anything yet.")    
    return redirect("/user/blogs/create")      

## CREATE, EDIT OR DELETE COMMENT OR REPLIES
def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Blog.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')

        ##### RECAPTCHA 
        
        res = check_recpatcha(request)

        if res != True:
            captchaVerificationFailedHandler(req=request, result=res)
            return redirect(f"/blog/{post.slug}")
        
        #####
       
        context = {
            'blogisActive': "active"
        }

        if parentSno=="":
            comment= Comment(comments= comment, user=user, post=post)
            comment.save()

            post.comments += 1
            post.save()

            messages.success(request, "Your comment has been posted successfully")

        else:
            parent = Comment.objects.get(sno=parentSno)
            comment= Comment(comments= comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

        
    return redirect(f"/blog/{post.slug}", context)   


def deleteComment(request, slug, sno):

   if request.method == "POST": 
    comment = Comment.objects.filter(sno=sno).first()

    if comment:
        if request.user == comment.user or request.user.is_superuser or request.user.is_staff: 
          comment.delete()

          if comment.parent is None: 
                post = Blog.objects.filter(slug=slug).first()
                post.comments -= 1
                post.save()

          messages.success(request, "Successfully deleted your comment or reply.")
          return redirect("/blog/{0}".format(slug))

        else:
            messages.warning(request, "You can only delete your comments and replies.")
            return redirect("/blog/{0}".format(slug))  

    else:
        messages.error(request, "This comment doesn't exists.")
        return redirect("/blog/{0}".format(slug))


   return redirect("/blog/{0}".format(slug))  


def editComment(request, slug, sno):

    if request.method == "POST":
        content = request.POST.get("comment", "default")
        comment = Comment.objects.filter(sno=sno).first()

        ##### RECAPTCHA 
        
        res = check_recpatcha(request)

        if res != True:
            captchaVerificationFailedHandler(req=request, result=res)
            return redirect("/blog/{0}".format(slug))
        
        #####
        
        if comment:
            if request.user == comment.user or request.user.is_superuser or request.user.is_staff:
                comment.comments = content
                comment.save()

                messages.success(request, "Successfully edited your comment or reply.")
                return redirect("/blog/{0}".format(slug))

            else:
                messages.warning(request, "You can only delete your comments and replies.")
                return redirect("/blog/{0}".format(slug))  

        else:
            messages.error(request, "This comment doesn't exists.")
            return redirect("/blog/{0}".format(slug))

    return redirect("/blog/{0}".format(slug)) 

