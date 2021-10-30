from django.contrib.messages import default_app_config
from django.db import models
from django.contrib.auth.models import User
# Models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    bio = models.CharField(max_length=100, null=True, blank=True),
    image = models.ImageField(default = 'default-avatar.png', upload_to = 'user_profile_pics')

    def __str__(self):
        return f'{self.user} Profile'