from django.db import models
from django.db.models import query
from django.db.models.fields import EmailField
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
   sno= models.AutoField(primary_key=True)
   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   name= models.CharField(max_length=255)
   phone= models.CharField(max_length=30)
   email= models.EmailField(max_length=100)
   content= models.TextField()
   timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

   def __str__(self):
          return "Message from " + self.name + ' - ' + self.email