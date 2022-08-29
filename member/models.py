from django.contrib.auth.models import User
from django.db import models


from uuid import uuid4
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):

         
    token = str(uuid4())
    user =  models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    beta = models.BooleanField(default=False, null=True, blank=True)
    bio  = models.CharField(max_length=300, null=True, blank=True)
    avatar = CloudinaryField(default="https://res.cloudinary.com/opensourcegames/image/upload/v1655312306/TextAnalyser/user_xa7wjp.svg", folder='TextAnalyser/user/user_{0}/images/profile'.format(token), null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"



    
