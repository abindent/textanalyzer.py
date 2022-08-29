from django.db import models
from django.utils.translation import gettext_lazy 

from django.contrib.auth.models import User 

# Create your models here.
class Application(models.Model):

    choices = (
            ("ST", "Apply for staff post"),
            ("AD", "Apply for admin post"),
            ("BW", "Apply for blog writer post"),
        )
     
    name = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    options = models.CharField(max_length=300, choices=choices, blank=True, null=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    application_status = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return "Application by " + self.user.username + ' for ' + self.options
    
