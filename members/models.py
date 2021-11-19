from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='user_profile_pics/',  default='default-avatar.png', null=True, blank=True)

    def __str__(self):
        return f"{self.user} Profile"

