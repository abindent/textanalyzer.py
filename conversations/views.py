import humanfriendly
from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def view_user(request, id):

    user = User.objects.filter(id=id).first()

    if user:
      account_created_at = user.date_joined
      now = datetime.now(timezone.utc)
  
      _account_age_time = int(now.strftime("%s")) - int(account_created_at.strftime("%s"))
      account_age = humanfriendly.format_timespan(_account_age_time)
      context = {"newuser": user, "account_age": account_age}

    else:
        context = {"newuser": None}  

    return render(request, 'conversations/user.html', context)

def get_all(request):
   results = User.objects.all()

   return render(request, 'conversations/index.html', {'allusers': results})