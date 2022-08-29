from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def privacy_policy(request):
    return render(request, "privacy/index.html")


def handler404(request, exception):
 
    
    problem = request.GET.get("type", False)

    if problem:
        if problem.__contains__("blog"):
           context = {"content_type": "blog", "context_type_page": "Blog Page", "link": "/blog/"}

        else:
            context = {"content_type":"keyword in all blogs", "context_type_page": "Blog Page", "link": "/blog/"}   

    else:
        context = {"content_type": "page", "context_type_page": "Home Page", "link": "/"}    

   

    response = render(request, 'error/404.html', context=context)
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, 'error/500.html')
    response.status_code = 500
    return response