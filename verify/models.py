from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class VerifyUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Verification Status"
    
