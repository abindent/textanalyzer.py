from django.shortcuts import render
from django.contrib import messages

from .models import SearchDB

# Create your views here.
def search(request):
    query = request.GET['q']

    if len(query) > 78:
        _all_post = SearchDB.objects.none()

    else:
        _all_title = SearchDB.objects.filter(title__icontains=query)
        _all_description = SearchDB.objects.filter(description__icontains=query)
        _all_slug = SearchDB.objects.filter(slug__icontains=query)
        _all_post = _all_title.union(_all_description, _all_slug)

    if _all_post.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query.")

    if query == "":
        messages.warning(request, "Please enter something to search")
        return redirect("/")

    params = {'allPosts': _all_post, 'query': query}
    return render(request, 'search/index.html', params)

